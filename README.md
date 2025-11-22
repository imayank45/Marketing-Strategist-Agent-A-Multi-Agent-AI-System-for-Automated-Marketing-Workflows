# Marketing-Strategist-Agent-A-Multi-Agent-AI-System-for-Automated-Marketing-Workflows
Built an automated multi-agent AI Marketing Strategist system using LangChain, RAG, and Streamlit to predict customer subscription likelihood and generate optimized campaign strategies for the banking domain.

🌟 Overview

The Marketing Strategist Agent is a Streamlit-based AI system designed to automate marketing strategy creation using a multi-agent architecture.
It combines:

A trained Logistic Regression model for customer conversion prediction

Three LLM-powered agents (strategy, review, optimization)

A central orchestrator to coordinate reasoning

A clean and modular production-ready folder structure

Users input customer features, and the system automatically:

Predicts conversion probability

Generates a marketing strategy

Reviews and evaluates the strategy

Produces a final optimized strategy

This project demonstrates strong skills in machine learning, LLM agents, full-stack development, reasoning pipelines, and product design—perfect for showcasing to recruiters.

🎯 Features

🤖 Multi-Agent AI Pipeline: Predictor → Strategist → Reviewer → Optimizer

📈 Conversion Prediction Model: Logistic Regression built on banking marketing dataset

🧠 Strategy Generation: GPT-4o-mini creates personalized marketing actions

📝 Strategy Review Engine: Highlights strengths, weaknesses, and gives a score

🔧 Strategy Optimization: Final polished output based on reviewer feedback

🖥️ Streamlit UI: Clean interface with editable customer feature inputs

🔗 Modular Architecture: Each agent is a standalone module

⚙️ Environment-Based LLM Support: Reads API key from .env

📦 Installation
Prerequisites

🐍 Python 3.9+

📦 pip

🔑 OpenAI API Key

📁 Logistic Regression Model: lr_model_selected.pkl

Dependencies

Install all required packages:

pip install -r requirements.txt

Setup
# Clone the repository
git clone https://github.com/your-username/marketing-strategist-agent.git
cd marketing-strategist-agent

# Add your OpenAI key
echo "OPENAI_API_KEY=your_key_here" > .env

# Run Streamlit app
streamlit run app.py

🛠️ Usage

Launch the Streamlit UI (http://localhost:8501).

Enter customer feature values in the input fields.

Click Run pipeline.

View:

📊 Prediction (conversion probability)

🧠 Generated strategy

📝 Reviewer insights

🚀 Optimized final strategy

Sample Input Fields
default
dummy_telephone
emp.var.rate
duration
loan
dummy_success
nr.employed
euribor3m
cons.price.idx
housing
marital_ordinal

🧠 Multi-Agent System Architecture
1️⃣ Predictor Agent

Loads the ML model

Arranges user data in predefined feature order

Returns:

- probability
- decision (0/1)
- raw preprocessed data

2️⃣ Strategy Agent

Converts probability into a focused marketing strategy.

Example:

Customer has medium probability of conversion.
Actions:
- Send personalized follow-up email
- Highlight interest-specific product features

3️⃣ Reviewer Agent

Evaluates the initial strategy and returns:

- Positive points
- Weaknesses
- Overall score


Example:

Strengths: Clear messaging.
Weaknesses: Lacks long-term nurturing workflow.
Score: 7.5/10

4️⃣ Optimizer Agent

Refines the strategy using reviewer feedback.

Example:

Final optimized strategy:
- Add 14-day follow-up loop
- Provide targeted EMI calculator
- Include personalization in SMS and email cadences

📁 Folder Structure
marketing-strategist-agent/
├── app.py
├── requirements.txt
├── .env
│
├── models/
│   ├── predictor.py
│   └── lr_model_selected.pkl
│
├── agents/
│   ├── orchestrator_agent.py
│   ├── strategy_agent.py
│   ├── retriever_agent.py
│   └── optimizer_agent.py
│
└── utils/
    └── __init__.py

💻 Technical Details
Backend

Streamlit

Python 3.9

dotenv for secure API key loading

Machine Learning

Logistic Regression

Predefined feature ordering

Pickle model loading

LLM Agents

Model: gpt-4o-mini

Used for strategy generation, feedback, and optimization

Lightweight, low-latency LLM calls

Pipeline Execution

Orchestrator connects all four agents

Each agent is modular and replaceable

Clean error handling

No tight coupling between agents

⚠️ Limitations

🤖 LLM output depends on API key availability

📉 Dummy/placeholder model may reduce accuracy if not replaced

📄 Strategies are AI-generated, not domain-certified

🌐 Internet required for OpenAI API calls

🚀 Future Improvements

📊 Add visualizations (probability trends, feature importance)

🧪 Add A/B Testing recommendations

🗄 Move ML model to ONNX / MLflow

💬 Add conversational UI for strategy changes

📚 Add historical customer database

🔧 Add caching for agent responses
