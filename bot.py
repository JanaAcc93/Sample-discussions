"""A simple rule-based chatbot that answers Q&A about Salesforce deployment components,
based on official Salesforce documentation."""
from knowledge_base import KNOWLEDGE_BASE, FALLBACK_ANSWER


def get_answer(question: str) -> str:
    """Return the best matching canned answer for a question, or a fallback."""
    question_lower = question.lower()
    is_definition_question = (
        any(
            phrase in question_lower
            for phrase in ("what is", "what's", "define", "explain")
        )
        and not any(
            phrase in question_lower
            for phrase in ("naming", "convention", "standard")
        )
    )

    best_match = None
    best_score = 0
    for entry in KNOWLEDGE_BASE:
        score = sum(1 for keyword in entry["keywords"] if keyword in question_lower)
        if score and is_definition_question and entry.get("answer_type") == "definition":
            score += 10
        if score > best_score:
            best_score = score
            best_match = entry

    return best_match["answer"] if best_match else FALLBACK_ANSWER


def main():
    print("Salesforce Deployment Q&A Bot — ask a question, or type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break
        if not question:
            continue
        print(f"Bot: {get_answer(question)}\n")


if __name__ == "__main__":
    main()
