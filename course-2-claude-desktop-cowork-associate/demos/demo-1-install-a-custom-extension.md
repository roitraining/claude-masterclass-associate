# Demo 1: Install a Custom Extension

**Course:** Claude Desktop Associate: Persistent Workspaces and Unattended Work (Claude MasterClass Associate, Course 2)
**Demo:** 1 of 7
**Time:** about 12 minutes

> Part of **[Claude Desktop Associate: Demos](README.md)**. Read the [guide preamble](README.md) for scenario notes and setup before you run this demo. The original combined guide is [`demos.md`](../demos.md).

---

**Learning objective:** Install a custom local extension that connects Claude to a persistent folder, and say how it differs from a per-session folder card and from a directory extension. Time: about 12 minutes.

**Files:** [`demo-files/knowledge-folder`](../demo-files/knowledge-folder) and a prepared `.mcpb` file (see the Instructor note).

**Context:** In Essentials, students gave Claude a folder for a single session. A custom local extension is installed once, stays installed, and runs a local MCP server on the machine. An `.mcpb` file is a zip that holds that local MCP server and a `manifest.json`. A directory extension is one published for general install. A custom extension is one you or your team built.

**Steps:**

1. Show the zip structure of the prepared `.mcpb` on screen. Point out `manifest.json` and the server file.
2. Open Claude Desktop. Go to **Settings**, then **Advanced settings**, then **Extension Developer**.
3. Select **Install Extension** and choose the prepared `.mcpb` file.
4. Read the install prompt aloud. Ask the room: what will this extension be able to reach?
5. Complete the install. Start a new conversation and ask: "List the files in the knowledge folder."
6. Ask: "What is the daily limit for a domestic wire in online banking? Name the file you used."
7. Open a second new conversation and ask the same question to show the extension persists without re-attaching a folder.

**Expected result:** The extension installs, Claude lists the **nine** files in the knowledge folder, and answers $25,000 citing `01-wire-transfer-procedure.md`. The second conversation answers without any folder being attached.

> **Eight or nine?** The folder holds nine files. The folder map `00-README-folder-map.md` tabulates the other **eight** and does not list itself, so "eight" is the count in the map and "nine" is the count on disk. Verified against the shipped folder and the extension on October 22, 2026.

> **Instructor note:** The facts we can confirm are the install path above and the `.mcpb` structure. The manifest fields, the server code, and the exact install prompt wording are not in our verified facts, so prepare the `.mcpb` in advance from Anthropic's MCPB documentation and rehearse it on the class VM. Whether Claude Desktop runs on the class VM operating system and installs custom extensions there is **unconfirmed**. If it does not, run this demo from the instructor's own machine. Team and Enterprise Owners can upload custom extensions for one-click team install, and a machine-level enterprise policy overrides in-app controls. Code signing and managed deployment for extensions are **unconfirmed**. Do not teach them as features.

> **Why this matters:** A persistent extension keeps its reach after the conversation ends. Install is a decision, not a convenience.

---

**Next:** [Demo 2: Design the Knowledge Folder](demo-2-design-the-knowledge-folder.md)


*Demo 1 of 7*
