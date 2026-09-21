"""Answers a comment posted on the pinned "guide me" GitHub Discussion using the
Salesforce deployment knowledge base, and posts the answer as a threaded reply.

Intended to run inside a GitHub Actions workflow triggered by the
`discussion_comment` event, scoped to a single designated hub discussion.
Reads the discussion node ID, the triggering comment's node ID/body/author
from environment variables and posts a threaded reply via the GitHub
GraphQL API using `gh api graphql`.
"""
import os
import subprocess
import sys

from bot import get_answer

# Never reply to our own bot comments — avoids an infinite reply loop.
BOT_LOGIN = "github-actions[bot]"

DISCLAIMER = (
    "\n\n---\n_I'm an automated bot answering based on official Salesforce "
    "documentation. Please verify details against Salesforce Help for your "
    "specific org/edition before relying on this for a production deployment._"
)

ADD_DISCUSSION_COMMENT_MUTATION = """
mutation($discussionId: ID!, $body: String!, $replyToId: ID!) {
  addDiscussionComment(
    input: { discussionId: $discussionId, body: $body, replyToId: $replyToId }
  ) {
    comment { id url }
  }
}
"""


def post_reply(discussion_id: str, reply_to_id: str, body: str) -> None:
    """Post `body` as a threaded reply to `reply_to_id` within the discussion."""
    result = subprocess.run(
        [
            "gh", "api", "graphql",
            "-f", f"query={ADD_DISCUSSION_COMMENT_MUTATION}",
            "-f", f"discussionId={discussion_id}",
            "-f", f"body={body}",
            "-f", f"replyToId={reply_to_id}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"Failed to post reply: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    print(result.stdout)


def main() -> None:
    comment_author = os.environ.get("COMMENT_AUTHOR", "")
    if comment_author == BOT_LOGIN:
        print("Skipping: comment was posted by the bot itself.")
        return

    discussion_id = os.environ["DISCUSSION_NODE_ID"]
    comment_id = os.environ["COMMENT_NODE_ID"]
    question = os.environ.get("COMMENT_BODY", "")

    answer = get_answer(question)
    post_reply(discussion_id, comment_id, answer + DISCLAIMER)


if __name__ == "__main__":
    main()
