
from faq_bot import answer
from golden import GOLDEN

from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import OllamaModel
from deepeval.test_case import LLMTestCase


model = OllamaModel(
    model="llama3.2:1b",
    base_url="http://localhost:11434",
    temperature=0
)

passed = 0
scores = []

print("\n========== ANSWER RELEVANCY EVALUATION ==========\n")

for index, case in enumerate(GOLDEN, start=1):

    question = case["q"]

    reply, source = answer(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=reply
    )

    metric = AnswerRelevancyMetric(
        model=model,
        threshold=0.5
    )

    metric.measure(test_case)

    score = metric.score
    scores.append(score)

    result = metric.is_successful()

    if result:
        passed += 1

    print(f"\nTest Case {index}: {question}")
    print("Bot Answer:", reply)
    print("Score:", round(score, 2))
    print("Result:", "PASS" if result else "FAIL")
    print("-" * 50)


print("\n========== FINAL REPORT ==========")

print("Total Questions:", len(GOLDEN))
print("Passed:", passed)
print("Failed:", len(GOLDEN) - passed)

print(
    "Average Relevancy:",
    round(sum(scores) / len(scores), 2)
)

print(
    "Pass Rate:",
    round((passed / len(GOLDEN)) * 100, 2),
    "%"
)

print("\n========== EVALUATION COMPLETED ==========")
