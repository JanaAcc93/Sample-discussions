# Sample-discussions

A simple rule-based chatbot that answers Q&A about Salesforce deployment components — change sets,
the Metadata API, managed/unlocked packages, scratch orgs, CI/CD, DevOps Center, permission sets vs.
profiles, sandboxes, validation deployments, destructive changes, deployment order, and metadata
naming conventions — based on official Salesforce documentation.

## Usage (CLI)

```bash
python bot.py
```

Ask a question, e.g. "what's the difference between managed and unlocked packages?", and the bot
replies with a canned answer. Type `exit` to quit.

## GitHub Discussions integration

A GitHub Actions workflow ([.github/workflows/answer-discussions.yml](.github/workflows/answer-discussions.yml))
automatically answers new posts in the repo's **Q&A** Discussions category:

1. Someone opens a new Discussion under the "Q&A" category asking about a Salesforce deployment topic.
2. The workflow triggers on the `discussion` event, runs `discussion_responder.py`, which matches the
   discussion title/body against `knowledge_base.py` using the same logic as `bot.py`.
3. The bot posts the matched answer (or a fallback message) as a reply comment on the discussion via
   the GitHub GraphQL API.

No extra setup is required beyond having GitHub Discussions enabled on the repository — the workflow
uses the built-in `GITHUB_TOKEN` with `discussions: write` permission.

## Extending

Add more Q&A pairs to `knowledge_base.py` — each entry has a list of `keywords` and an `answer`.
The bot matches your question against these keywords and returns the best-scoring answer.
