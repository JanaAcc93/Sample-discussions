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

## GitHub Discussions integration ("Guide Me" bot thread)

<p align="center">
   <img src="assets/guide-me.gif" alt="Animated Guide Me compass" width="112">
</p>

A single pinned Discussion acts as the entry point to the bot — click into it, post your question as
a comment, and the bot replies inline in the same thread.

**One-time setup:**

1. Create a new Discussion (see suggested title/body below) and pin it from the **⋯** menu so it's
   always visible at the top of the Discussions tab.
2. Note its discussion number (from the URL, e.g. `.../discussions/5` → `5`).
3. In the repo, go to **Settings → Secrets and variables → Actions → Variables** and add a repository
   variable named `GUIDE_DISCUSSION_NUMBER` set to that number.

Suggested title/body for the pinned discussion:

> **Title:** 🧭 Guide Me — Ask the Salesforce Deployment Bot
>
> **Body:** Reply to this discussion with your question about Salesforce deployment components
> (change sets, packaging, scratch orgs, CI/CD, DevOps Center, permission sets, naming conventions,
> etc.) and the bot will answer inline.

**How it works:** the workflow ([.github/workflows/answer-discussion-comments.yml](.github/workflows/answer-discussion-comments.yml))
triggers on the `discussion_comment` event, checks that the comment was posted on the discussion
number stored in `GUIDE_DISCUSSION_NUMBER` (and isn't from the bot itself), runs
`discussion_comment_responder.py` to match the comment text against `knowledge_base.py` (same logic
as `bot.py`), and posts the answer as a threaded reply via the GitHub GraphQL API using the built-in
`GITHUB_TOKEN` with `discussions: write` permission.

## Extending

Add more Q&A pairs to `knowledge_base.py` — each entry has a list of `keywords` and an `answer`.
The bot matches your question against these keywords and returns the best-scoring answer.
