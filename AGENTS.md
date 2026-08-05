# AGENTS.md — Repository AI agent instructions

Purpose
-------
This file gives minimal, actionable guidance for AI coding agents interacting with this repository. It documents a repo-level signal `chat.disableAIFeatures` that tells agents to operate in a read-only, advisory mode.

When to set `chat.disableAIFeatures`
- Sensitive code (credentials, secrets, cryptography)
- Legal/licensed content or third-party code where copying is restricted
- Security reviews, audits, or any regulatory/compliance work
- Instructor/assessment code or private student submissions

Behavior when `chat.disableAIFeatures: true`
- Do not modify files or apply patches automatically.
- Do not execute or run repository code or tests.
- Provide read-only analysis, suggestions, and step-by-step manual instructions.
- When suggesting changes, present them as explicit unified diffs or patch text and label them "Suggested — do not apply".
- Flag any uncertainty and ask for human confirmation before making edits.

How to use this signal
- Human or tooling that invokes an AI agent should pass the argument `chat.disableAIFeatures` to indicate this mode. Example values: `true` or `on`.
- Agents should check for this flag at session start and follow the rules above for the whole session.

Examples
- "Run security review — chat.disableAIFeatures: true": agent returns a code audit and explicit suggested patches but does not modify files.

Contact
- If the agent needs escalation, mention the repository owners or open an issue describing what it needs to change.

Minimal and link-first
- Keep AGENTS.md short. Link to existing docs (CONTRIBUTING, README) for project-specific workflows rather than duplicating them.
