# app.py
import streamlit as st
import os
import json
from dotenv import load_dotenv
from agents.prediction_agent import PredictionAgent
from agents.strategy_agent import StrategyAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.optimizer_agent import OptimizerAgent
from agents.orchestrator_agent import Orchestrator
from config.settings import MODEL_PATH, OPENAI_API_KEY

load_dotenv()

FEATURE_ORDER = ['default','dummy_telephone','emp.var.rate','duration','loan','dummy_success','nr.employed','euribor3m','cons.price.idx','housing','marital_ordinal']

st.set_page_config(page_title='Marketing Strategist Agent', layout='wide')
st.title('Marketing Strategist Agent — Bank Domain')

st.sidebar.header('Settings')
st.sidebar.write(f'OPENAI_API_KEY set: {bool(OPENAI_API_KEY)}')

st.markdown('### Enter feature values')
raw = {}
cols = st.columns(3)
i = 0
for feat in FEATURE_ORDER:
    with cols[i % 3]:
        raw[feat] = [st.number_input(feat, value=0.0, format='%f')]
    i += 1

docs_context = ""
if st.checkbox("Load RAG docs (if available)"):
    st.write("Ensure PDFs exist in rag/brand_docs and you ran rag/ingest_pdf.py")
    docs_context = st.text_area("Optional context summary (manual)")

if st.button('Run pipeline'):
    if not os.path.exists(MODEL_PATH):
        st.error('Model pickle not found. Run scripts/create_dummy_model.py or place your .pkl in models/')
    else:
        predictor = PredictionAgent(MODEL_PATH, FEATURE_ORDER)
        strategy_agent = StrategyAgent()
        # If you want RAG-based evaluation, ensure rag/chroma_db exists and pass docs_dir parameter to EvaluatorAgent
        evaluator = EvaluatorAgent()

        optimizer = OptimizerAgent()
        orchestrator = Orchestrator(predictor, strategy_agent, evaluator, optimizer)

        with st.spinner('Running pipeline...'):
            out = orchestrator.run_pipeline(raw, docs_context)

        st.subheader('Prediction (Agent 1)')
        st.json(out['prediction'])

        st.subheader('Initial Strategy (Agent 2)')
        st.write(out['initial_strategy'])

        st.subheader('Evaluations (Agent 3)')
        for idx, eval_obj in enumerate(out.get('evaluations', [])):
            st.markdown(f'**Iteration {idx+1}**')
            if hasattr(eval_obj, 'json'):
                st.json(json.loads(eval_obj.json()))
            else:
                st.write(eval_obj)

        st.subheader('Final Strategy')
        st.write(out['final_strategy'])
