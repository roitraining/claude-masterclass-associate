# Pinecrest Knowledge Folder: the custom extension for Demo 1, Demo 2 and Lab 1

This is the `.mcpb` the course needs. Earlier versions of the guides told the facilitator
to build one from Anthropic's MCPB documentation; this is that asset, built and tested.

## What it is

A local MCP server that gives Claude **read-only** access to **one folder you choose**.
It is deliberately small: no dependencies, no network access, no writes, about 200 lines
you can read before an IT review meeting.

Three tools:

| Tool | What it does |
|---|---|
| `list_documents` | Lists every document in the folder |
| `read_document` | Reads one document by name |
| `search_documents` | Searches all documents for a phrase, returns matching lines |

## Why it is built this way

**No dependencies.** It speaks the MCP protocol directly over stdio rather than importing
the SDK, so the bundle is a few kilobytes, needs no `npm install`, and a security reviewer
can read all of it. Claude Desktop ships its own Node runtime on macOS and Windows, so
students install nothing.

**Read-only, one folder, enforced.** Every path is resolved and checked against the folder
the user selected. A request for anything outside it is refused with a message that names
the folder. **This refusal is what Demo 2 demonstrates** — the folder scope is a software
boundary you can actually test, which is the distinction Module 3 teaches.

Verified refusals: `../keep-out-of-the-workspace/hr-salary-bands.csv`, the Windows
backslash form, and a fully absolute path. All three are rejected.

## Build the .mcpb

The packaged file is already here as `pinecrest-knowledge.mcpb`. Rebuild it only if you
change the server.

An `.mcpb` is a zip with `manifest.json` **at the root** — not inside a folder. That is the
opposite of a Skill zip, which must contain its folder. Getting this wrong is the most
common packaging mistake.

**Windows (PowerShell), no tooling required:**

```powershell
cd custom-extension
Compress-Archive -Path manifest.json,server -DestinationPath pinecrest-knowledge.zip -Force
Move-Item pinecrest-knowledge.zip pinecrest-knowledge.mcpb -Force
```

**macOS or Linux:**

```bash
cd custom-extension
zip -r pinecrest-knowledge.mcpb manifest.json server
```

**Or with Anthropic's CLI**, which validates the manifest as it packs:

```bash
npm install -g @anthropic-ai/mcpb
mcpb pack
```

## Install it

Any of these work. Double-click is easiest in a classroom:

1. **Double-click** `pinecrest-knowledge.mcpb`
2. **Drag and drop** it onto the Claude Desktop window
3. **Settings > Extensions > Advanced settings > Install Extension…**

> The deck and guides teach path 3. Confirm the exact menu wording on the class build
> before you teach it — Anthropic's documentation and the shipped product have disagreed
> on settings paths before.

During install Claude Desktop shows a settings screen generated from `manifest.json` and
asks for the **Knowledge folder**. Point it at the `knowledge-folder` directory from the
course files. Claude can read that folder and nothing else.

## Test it before class

From this directory, with Node installed:

```bash
node server/index.js /full/path/to/knowledge-folder
```

It prints `[pinecrest-knowledge] serving <path>` to stderr and then waits for JSON-RPC on
stdin. If you see that line, the server starts cleanly. Press Ctrl+C to stop.

In Claude Desktop, confirm with these three, which are Demo 1 and Demo 2 in miniature:

1. "List the files in the knowledge folder." → **nine documents**
2. "What is the daily limit for a domestic wire in online banking? Name the file you used."
   → **$25,000**, citing `01-wire-transfer-procedure.md`
3. "What is the branch manager salary band?" → **not covered in the knowledge folder**

> **On the file count:** the folder holds **nine** files. The folder map
> `00-README-folder-map.md` tabulates the other **eight** and does not list itself. If a
> demo script says "eight files", that is the count in the map, not the count on disk.

## Editing it for your own classroom

The scenario nouns live in the knowledge folder, not in this server, so you can swap
Pinecrest for a healthcare or government scenario by replacing the documents. Change
`READABLE` in `server/index.js` if you add file types beyond `.md`, `.csv`, `.txt`
and `.json`.
