
from faq_bot import answer, KNOWLEDGE

from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric
)

from deepeval.models import OllamaModel
from deepeval.test_case import LLMTestCase


# Connect DeepEval to local Ollama model
model = OllamaModel(
    model="llama3.2:1b",
    base_url="http://localhost:11434",
    temperature=0
)


# Ask the FAQ bot a question
question = "My fan remote stopped working. What should I do?"

reply, source = answer(question)


# Find the matching knowledge-base information
retrieval_context = [
    article["text"]
    for article in KNOWLEDGE
    if article["id"] == source
]


# Create evaluation test case
test_case = LLMTestCase(
    input=question,
    actual_output=reply,
    retrieval_context=retrieval_context
)


# Metric 1: Answer Relevancy
relevancy = AnswerRelevancyMetric(
    model=model,
    threshold=0.5
)


# Metric 2: Faithfulness
faithfulness = FaithfulnessMetric(
    model=model,
    threshold=0.5
)


# Run evaluations
relevancy.measure(test_case)
faithfulness.measure(test_case)


# Display results
print("\n========== DEEPEVAL RESULTS ==========")

print("\nQuestion:", question)
print("Bot Answer:", reply)

print("\n--- Answer Relevancy ---")
print("Score:", relevancy.score)
print("Reason:", relevancy.reason)
print("Passed:", relevancy.is_successful())

print("\n--- Faithfulness ---")
print("Score:", faithfulness.score)
print("Reason:", faithfulness.reason)
print("Passed:", faithfulness.is_successful())
