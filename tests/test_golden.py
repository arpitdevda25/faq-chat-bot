
import pytest

from faq_bot import answer
from golden import GOLDEN


@pytest.mark.parametrize("case", GOLDEN)
def test_faq_answer_matches_golden_case(case):

    # Get chatbot response
    reply, source = answer(case["q"])

    # Check required facts
    for fact in case["must"]:
        assert fact.lower() in reply.lower()

    # Check correct knowledge article
    assert source == case["source"]

    # Check refusal for unsupported questions
    if case["source"] is None:
        assert "don't know" in reply.lower()
