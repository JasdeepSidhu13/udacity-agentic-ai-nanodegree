# AGENTS.md

## Cursor Cloud specific instructions

This repository is **documentation-only**. It contains a single `README.md` that
acts as the portfolio hub for the Udacity Agentic AI Nanodegree work and links
out to four separate external project repositories. There is intentionally:

- no application source code in this repo,
- no dependency manifest (no `requirements.txt`, `package.json`, etc.),
- no build system, no automated tests, and no lint configuration.

As a result there is nothing to install, build, lint, or test here, and the
startup update script is a no-op.

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
