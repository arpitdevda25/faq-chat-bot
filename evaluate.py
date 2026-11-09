
from faq_bot import answer
from golden import GOLDEN


def evaluate(cases, gate=0.90):

    total = len(cases)

    passed = 0
    correctness_passed = 0
    groundedness_passed = 0
    refusal_passed = 0

    print("\n========== FAQ BOT EVALUATION ==========\n")

    for index, case in enumerate(cases, start=1):

        question = case["q"]
        required_facts = case["must"]
        expected_source = case["source"]

        reply, actual_source = answer(question)

        # 1. Correctness check
        correctness = all(
            fact.lower() in reply.lower()
            for fact in required_facts
        )

        # 2. Groundedness check
        groundedness = actual_source == expected_source

        # 3. Refusal check (only for unsupported questions)
        if expected_source is None:
            refusal = (
                actual_source is None
                and "don't know" in reply.lower()
            )
        else:
            refusal = True

        if correctness:
            correctness_passed += 1

        if groundedness:
            groundedness_passed += 1

        if refusal:
            refusal_passed += 1

        overall = correctness and groundedness and refusal

        if overall:
            passed += 1

        print(f"Test Case {index}: {question}")
        print("Correctness:", "PASS" if correctness else "FAIL")
        print("Groundedness:", "PASS" if groundedness else "FAIL")

        if expected_source is None:
            print("Refusal:", "PASS" if refusal else "FAIL")

        print("Overall:", "PASS" if overall else "FAIL")
        print("-" * 50)

    if total == 0:
        print("No test cases available.")
        return

    # Calculate percentages
    pass_rate = passed / total * 100
    correctness_rate = correctness_passed / total * 100
    groundedness_rate = groundedness_passed / total * 100
    refusal_rate = refusal_passed / total * 100

    # Final report
    print("\n========== FINAL EVALUATION REPORT ==========")

    print(f"Total Test Cases: {total}")
    print(f"Overall Passed: {passed}")
    print(f"Overall Failed: {total - passed}")

    print(f"\nCorrectness Rate: {correctness_rate:.2f}%")
    print(f"Groundedness Rate: {groundedness_rate:.2f}%")
    print(f"Refusal Check Pass Rate: {refusal_rate:.2f}%")
    print(f"Overall Pass Rate: {pass_rate:.2f}%")

    print(f"\nRelease Gate: {gate * 100:.0f}%")

    if pass_rate >= gate * 100:
        print("RELEASE: ALLOWED")
    else:
        print("RELEASE: BLOCKED")


evaluate(GOLDEN)
