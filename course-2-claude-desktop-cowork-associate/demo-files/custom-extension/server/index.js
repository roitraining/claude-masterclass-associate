#!/usr/bin/env node
/**
 * Pinecrest Knowledge Folder - a local MCP server for Claude MasterClass Associate 2.
 *
 * Exposes one folder, read-only, over stdio. No dependencies, so the bundle needs no
 * npm install and a facilitator (or an IT reviewer) can read the whole server at once.
 *
 * Every path is resolved and checked against the configured root before any read, so a
 * request for a file outside the folder is refused. That refusal is the point of Demo 2.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const PROTOCOL_VERSION = '2025-06-18';
const SERVER_INFO = { name: 'pinecrest-knowledge', version: '1.0.0' };

// Claude Desktop passes the folder the user picked as the first argument.
const ROOT = path.resolve(process.argv[2] || process.cwd());

// Only these extensions are served. Keeps the demo predictable and avoids binaries.
const READABLE = new Set(['.md', '.csv', '.txt', '.json']);

const log = (msg) => process.stderr.write(`[pinecrest-knowledge] ${msg}\n`);

/** Resolve a caller-supplied relative path, refusing anything outside ROOT. */
function safeResolve(relish) {
  const full = path.resolve(ROOT, relish);
  const rel = path.relative(ROOT, full);
  if (rel === '' || rel.startsWith('..') || path.isAbsolute(rel)) {
    throw new Error(
      `Refused: "${relish}" is outside the knowledge folder. ` +
      `This server only reads files inside ${ROOT}.`
    );
  }
  return full;
}

/** Every readable file under ROOT, as paths relative to ROOT, sorted. */
function listFiles() {
  const out = [];
  (function walk(dir) {
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch (err) {
      log(`cannot read ${dir}: ${err.message}`);
      return;
    }
    for (const e of entries) {
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (READABLE.has(path.extname(e.name).toLowerCase())) {
        out.push(path.relative(ROOT, full).split(path.sep).join('/'));
      }
    }
  })(ROOT);
  return out.sort();
}

const TOOLS = [
  {
    name: 'list_documents',
    description:
      'List every document in the Pinecrest knowledge folder. Use this first to see what ' +
      'is available before answering a question about procedures, policies or fees.',
    inputSchema: { type: 'object', properties: {}, additionalProperties: false },
  },
  {
    name: 'read_document',
    description:
      'Read one document from the Pinecrest knowledge folder by its relative path, as ' +
      'returned by list_documents. Cite the file name in any answer that uses it.',
    inputSchema: {
      type: 'object',
      properties: {
        file: {
          type: 'string',
          description: 'Relative path, for example "01-wire-transfer-procedure.md".',
        },
      },
      required: ['file'],
      additionalProperties: false,
    },
  },
  {
    name: 'search_documents',
    description:
      'Search the knowledge folder for a phrase and return matching lines with their file ' +
      'names. Use when you do not know which document covers a question.',
    inputSchema: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Text to look for. Case insensitive.' },
      },
      required: ['query'],
      additionalProperties: false,
    },
  },
];

function callTool(name, args) {
  if (name === 'list_documents') {
    const files = listFiles();
    return `Knowledge folder: ${ROOT}\n${files.length} document(s):\n\n` +
      files.map((f) => `- ${f}`).join('\n');
  }

  if (name === 'read_document') {
    const file = String((args && args.file) || '');
    if (!file) throw new Error('read_document needs a "file" argument.');
    const full = safeResolve(file);
    if (!fs.existsSync(full) || !fs.statSync(full).isFile()) {
      throw new Error(`Not found: "${file}". Call list_documents to see what exists.`);
    }
    if (!READABLE.has(path.extname(full).toLowerCase())) {
      throw new Error(`Refused: "${file}" is not a readable document type.`);
    }
    return `--- ${file} ---\n${fs.readFileSync(full, 'utf8')}`;
  }

  if (name === 'search_documents') {
    const q = String((args && args.query) || '').toLowerCase();
    if (!q) throw new Error('search_documents needs a "query" argument.');
    const hits = [];
    for (const f of listFiles()) {
      const lines = fs.readFileSync(path.join(ROOT, f), 'utf8').split(/\r?\n/);
      lines.forEach((line, i) => {
        if (line.toLowerCase().includes(q)) hits.push(`${f}:${i + 1}: ${line.trim()}`);
      });
    }
    return hits.length
      ? `${hits.length} match(es) for "${args.query}":\n\n${hits.join('\n')}`
      : `No match for "${args.query}" in the knowledge folder.`;
  }

  throw new Error(`Unknown tool: ${name}`);
}

// ---------------------------------------------------------------- JSON-RPC over stdio

function send(msg) {
  process.stdout.write(JSON.stringify(msg) + '\n');
}

function handle(req) {
  const { id, method, params } = req;

  // Notifications have no id and take no reply.
  if (id === undefined || id === null) return;

  try {
    if (method === 'initialize') {
      const asked = params && params.protocolVersion;
      return send({
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: typeof asked === 'string' ? asked : PROTOCOL_VERSION,
          capabilities: { tools: {} },
          serverInfo: SERVER_INFO,
        },
      });
    }

    if (method === 'tools/list') {
      return send({ jsonrpc: '2.0', id, result: { tools: TOOLS } });
    }

    if (method === 'tools/call') {
      const { name, arguments: args } = params || {};
      try {
        const text = callTool(name, args);
        return send({ jsonrpc: '2.0', id, result: { content: [{ type: 'text', text }] } });
      } catch (err) {
        // Tool failures are results with isError, not protocol errors, so Claude can
        // read the refusal and explain it to the room.
        return send({
          jsonrpc: '2.0',
          id,
          result: { content: [{ type: 'text', text: err.message }], isError: true },
        });
      }
    }

    if (method === 'ping') return send({ jsonrpc: '2.0', id, result: {} });

    return send({
      jsonrpc: '2.0',
      id,
      error: { code: -32601, message: `Method not found: ${method}` },
    });
  } catch (err) {
    send({ jsonrpc: '2.0', id, error: { code: -32603, message: String(err.message) } });
  }
}

let buffer = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => {
  buffer += chunk;
  let nl;
  while ((nl = buffer.indexOf('\n')) !== -1) {
    const line = buffer.slice(0, nl).trim();
    buffer = buffer.slice(nl + 1);
    if (!line) continue;
    let req;
    try {
      req = JSON.parse(line);
    } catch (err) {
      log(`bad JSON: ${err.message}`);
      continue;
    }
    handle(req);
  }
});
process.stdin.on('end', () => process.exit(0));

log(`serving ${ROOT}`);
