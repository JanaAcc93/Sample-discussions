"""Answers a GitHub Discussion automatically using the Salesforce deployment
knowledge base, and posts the answer as a reply comment.

Intended to run inside a GitHub Actions workflow triggered by the `discussion`
event. Reads the discussion's node ID, title, and body from environment
variables and posts a reply via the GitHub GraphQL API using `gh api graphql`.
"""
import os
import subprocess
import sys

from bot import get_answer

DISCLAIMER = (
    "\n\n---\n_I'm an automated bot answering based on official Salesforce "
    "documentation. Please verify details against Salesforce Help for your "
    "specific org/edition before relying on this for a production deployment._"
)

ADD_DISCUSSION_COMMENT_MUTATION = """
mutation($discussionId: ID!, $body: String!) {
  addDiscussionComment(input: { discussionId: $discussionId, body: $body }) {
    comment { id url }
  }
}
"""


def post_comment(discussion_id: str, body: str) -> None:
    """Post `body` as a new top-level comment on the discussion via the GraphQL API."""
    result = subprocess.run(
        [
            "gh", "api", "graphql",
            "-f", f"query={ADD_DISCUSSION_COMMENT_MUTATION}",
            "-f", f"discussionId={discussion_id}",
            "-f", f"body={body}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"Failed to post comment: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    print(result.stdout)


def main() -> None:
    discussion_id = os.environ["DISCUSSION_NODE_ID"]
    title = os.environ.get("DISCUSSION_TITLE", "")
    body_text = os.environ.get("DISCUSSION_BODY", "")

    question = f"{title}\n{body_text}".strip()
    answer = get_answer(question)
    post_comment(discussion_id, answer + DISCLAIMER)


if __name__ == "__main__":
    main()
