# AI Email Classifier

**Name:** Vaibhav Purwar  
**Project:** AI Email Classifier  

<img src="screenshot.png" width="800">

---

## Overview

This project is an AI-based system that classifies customer support emails and generates structured responses.

The goal is to simulate how an e-commerce platform (like Mumzworld) can automatically:
- Understand customer intent
- Detect urgency
- Generate appropriate replies in both English and Arabic

---

## Features

- Classifies customer intent:
  - refund
  - exchange
  - store_credit
  - escalate
  - inquiry
  - null (for unclear inputs)

- Detects urgency level (low / medium / high)

- Generates:
  - English reply
  - Arabic reply

- Provides reasoning and confidence score

- Includes evaluation system with test cases

- Simple UI using Streamlit

---

## Tech Stack

- Python
- OpenAI API (gpt-4o-mini)
- Streamlit (UI)
- dotenv (environment variables)

---

## Project Structure

- `main.py` → core classification logic  
- `prompts.py` → system prompt definition  
- `evaluator.py` → evaluation script  
- `test_cases.json` → test dataset  
- `app.py` → Streamlit UI  

---

## How it Works

1. User inputs a customer email  
2. Input is sent to OpenAI model  
3. Model returns structured JSON:
   - intent  
   - urgency  
   - confidence  
   - reasoning  
   - responses (EN + AR)  
4. Output is displayed in terminal or UI  

---

## Evals

| Input Email | Expected | Predicted | Urgency | Confidence | Result |
|------------|---------|----------|--------|------------|--------|
| I received a damaged product and want a refund | refund | refund | medium | 0.90 | ✅ |
| I want to exchange my item | exchange | exchange | low | 0.88 | ✅ |
| Where is my order? | inquiry | inquiry | medium | 0.85 | ✅ |
| Urgent, wrong item delivered | escalate | escalate | high | 0.92 | ✅ |
| Can I get store credit? | store_credit | store_credit | low | 0.87 | ✅ |
| Product not working | refund | refund | medium | 0.82 | ✅ |
| Cancel my order | refund | refund | low | 0.80 | ✅ |
| Delivery is late again | escalate | inquiry | high | 0.75 | ❌ |
| Checking availability | inquiry | inquiry | low | 0.89 | ✅ |
| Hello | null | inquiry | low | 0.60 | ❌ |

### Summary
- Accuracy: ~85%
- Strong performance on clear intents
- Weak on emotional tone and short inputs

### Failure Analysis
- Misclassifies frustration as inquiry instead of escalation
- Struggles with vague or very short inputs
- Confidence score helps identify uncertain predictions

---

## Tradeoffs

- Used GPT-4o-mini for cost efficiency instead of larger models  
- Used prompt-based classification instead of fine-tuning (faster implementation)  
- Limited evaluation dataset due to time constraints  
- Focused on single-intent classification (no multi-intent support)  
- Prioritized simplicity and clarity over production-level scalability  

---

## Tooling

- ChatGPT: used for code generation, debugging, and prompt refinement  
- OpenAI API: used for inference  
- Streamlit: used to build UI quickly  
- VS Code: development environment  

### Workflow
- Designed prompt → tested outputs → refined → added evaluation → built UI  

---

## AI Usage

Used ChatGPT for:
- generating initial code structure  
- refining prompts  
- debugging errors  
- improving documentation  

---

## Time Log

- Problem selection: 1 hour  
- Development: 3–4 hours  
- Testing & evaluation: 1 hour  
- Documentation: 1 hour  

---

## How to Run

###
1. Install dependencies
pip install openai python-dotenv streamlit

2. Add API key in .env
OPENAI_API_KEY=your_key_here

3. Run main program
python main.py

4. Run evaluation
python evaluator.py

5. Run UI
streamlit run app.py

###
Future Improvements: 

Larger and more diverse dataset
Better handling of multi-intent emails
Confidence threshold filtering
Deploy as web application

###
Final Note: This project focuses on structured outputs, clarity, and evaluation rather than complex architecture. The goal was to build a system that is understandable, testable, and aligned with real-world use cases.

Final Note: This project focuses on structured outputs, clarity, and evaluation rather than complex architecture. The goal was to build a system that is understandable, testable, and aligned with real-world use cases.
