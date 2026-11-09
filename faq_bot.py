
import re

# Knowledge Base
KNOWLEDGE = [
    {
        "id": "kb-01",
        "text": "If the remote stops working, replace both batteries and stand within 5 metres of the fan."
    },
    {
        "id": "kb-02",
        "text": "The fan supports 2.4 GHz Wi-Fi only and does not support 5 GHz Wi-Fi."
    },
    {
        "id": "kb-03",
        "text": "The motor warranty is valid only with the purchase invoice."
    }
]

# Default response for unsupported questions
REFUSAL = "Sorry, I don't know that. Please contact support."

# Common words ignored during keyword matching
STOP_WORDS = {
    "the", "is", "a", "an", "if", "to", "and",
    "of", "with", "what", "do", "i", "my",
    "does", "it", "work", "for", "only", "that"
}


# Convert text into searchable keywords
def tokenize(text):
    words = set(re.findall(r"[a-z0-9]+", text.lower()))
    return words - STOP_WORDS


# Generate an answer based on keyword matching
def answer(question):

    question_words = tokenize(question)

    if not question_words:
        return REFUSAL, None

    best_score = 0
    best_article = None

    for article in KNOWLEDGE:

        article_words = tokenize(article["text"])

        score = len(question_words & article_words)

        if score > best_score:
            best_score = score
            best_article = article

    # Minimum matching threshold
    if best_score < 2:
        return REFUSAL, None

    return best_article["text"], best_article["id"]


# Run chatbot directly
if __name__ == "__main__":

    print("Welcome to Smart Fan Support!")
    print("Type 'exit' to stop the chatbot.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        reply, source = answer(question)

        print("Chatbot:", reply)
        print("Source:", source)
        print()
