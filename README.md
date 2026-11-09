
# Smart Fan FAQ Bot – AI Quality Engineering

A knowledge-based FAQ chatbot with a testing and evaluation framework designed to assess response correctness, answer relevancy, faithfulness, and refusal behaviour.

## Project Overview

This project demonstrates fundamental concepts of AI Quality Engineering by combining a rule-based FAQ chatbot with automated functional testing and LLM-based evaluation.

The chatbot retrieves answers from a predefined knowledge base using keyword matching. Its responses are evaluated using pytest and DeepEval with a locally running Ollama model.

## Key Features

- Knowledge-based FAQ chatbot
- Keyword-based question matching
- Handling of unsupported questions
- Golden dataset containing 12 test cases
- Automated functional testing using pytest
- Parameterized regression testing
- Answer Relevancy evaluation using DeepEval
- Faithfulness evaluation using DeepEval
- Local LLM evaluation using Ollama
- No OpenAI API key required

## Tech Stack

- Python
- pytest
- DeepEval
- Ollama
- Llama 3.2 (1B)

## Project Structure

```text
faq-chat-bot/
│
├── faq_bot.py
├── golden.py
├── evaluate.py
├── deepeval_test.py
├── deepeval_full_test.py
│
├── tests/
│   └── test_golden.py
│
├── README.md
└── requirements.txt
```

## Testing and Evaluation

### 1. Functional Testing

Run:

```bash
python -m pytest -v
```

The golden dataset contains 12 test cases covering:

- Remote-related questions
- Wi-Fi-related questions
- Warranty-related questions
- Unsupported questions

Latest functional test result:

- Total test cases: 12
- Passed: 12
- Failed: 0
- Pass rate: 100%

### 2. DeepEval – Answer Relevancy

Run:

```bash
python deepeval_full_test.py
```

Answer Relevancy evaluates whether chatbot responses address the user's questions.

### 3. DeepEval – Faithfulness

Run:

```bash
python deepeval_test.py
```

Faithfulness evaluates whether the chatbot's responses are supported by the supplied retrieval context.

## Local Model Setup

Install Ollama and download the model:

```bash
ollama run llama3.2:1b
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Project Learning Outcomes

- Understanding AI Quality Engineering
- Designing golden datasets
- Writing parameterized pytest tests
- Performing regression testing
- Understanding Answer Relevancy and Faithfulness
- Using local LLMs as evaluation judges
- Interpreting evaluation scores and identifying potential quality issues

## Limitations

- The chatbot uses keyword matching rather than a generative LLM.
- The knowledge base contains a limited number of FAQ articles.
- LLM evaluation scores can vary because of the evaluator model's limitations.
- Results should not be treated as production-level quality guarantees.

## Future Improvements

- Expand the FAQ knowledge base.
- Improve retrieval using semantic search.
- Add more evaluation metrics.
- Integrate a generative LLM.
- Build a web-based chatbot interface.
- Generate automated evaluation reports.
