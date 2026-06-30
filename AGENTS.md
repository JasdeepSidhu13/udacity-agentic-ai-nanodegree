# AGENTS.md

## Cursor Cloud specific instructions

This repository is the portfolio hub for the Udacity Agentic AI Nanodegree work.
`README.md` is the entry point, and the **full source of all four projects is now
vendored into same-named subdirectories**:

- `AgentsVille-Trip-Planner/`
- `AgenticWorkFlow/`
- `Udaplay/`
- `Multi-Agent-System/`

These directories are snapshots copied from the linked source repositories (with
their nested `.git`, `.DS_Store`, and `.ipynb_checkpoints` removed). They are
**not** git submodules, so updates pushed to the upstream repos do not flow here
automatically — re-vendor manually if you need to refresh them.

The repository root itself has no aggregate dependency manifest, build system,
automated tests, or lint config, so the startup update script is a no-op. Each
vendored project carries its own dependencies and run instructions (see each
project's `requirements.txt` / `README.md` and the per-project "How to Explore"
sections in the root `README.md`). Those projects require their own `.env` files
(OpenAI/Tavily keys) to actually run.

### "Running" this repo

The only meaningful artifact is `README.md`. The natural dev activity is
previewing the rendered Markdown. A quick way to preview locally:

```bash
pip install --break-system-packages markdown   # one-off, not a repo dependency
python3 -c "import markdown,sys; open('/tmp/readme.html','w').write(markdown.markdown(open('README.md').read(), extensions=['tables','fenced_code']))"
python3 -m http.server 8099 --directory /tmp   # then open /tmp/readme.html
```

Note: the system `python3 -m venv` lacks `ensurepip`, so use
`pip install --break-system-packages` (or `pip install --user`) for any preview
tooling rather than creating a virtualenv.

### Verifying the portfolio's "core function"

The portfolio's value is that its links resolve to real, accessible
repositories. All four GitHub project links return HTTP 200. The
`https://www.linkedin.com/in/jssidhu9/` link returns HTTP `999`, which is
LinkedIn's standard anti-bot response and not a broken link.

### The actual projects

The four linked projects (AgentsVille Trip Planner, Agentic Workflow, UdaPlay,
Multi-Agent System) live in their own repositories and each has its own
dependencies, `.env` requirements (OpenAI/Tavily keys), and run instructions.
They are **not** part of this repo; see the per-project "How to Explore"
sections in `README.md`.
