import streamlit as st
from dotenv import load_dotenv
import os
from models.predictor import PredictorAgent
from agents.orchestrator_agent import Orchestrator
from agents.strategy_agent import StrategyAgent
load_dotenv()


FEATURE_ORDER = [
    'default','dummy_telephone','emp.var.rate','duration',
    'loan','dummy_success','nr.employed','euribor3m',
    'cons.price.idx','housing','marital_ordinal'
]

PICKLE_PATH = "models/lr_model_selected.pkl"

st.set_page_config(page_title="Marketing Strategist Agent", layout="wide")
st.title("Marketing Strategist Agent — Banking Domain (User Input Version)")

st.markdown("Provide all feature values below and run the full multi-agent pipeline.")

# Sidebar: settings
st.sidebar.header("Settings")
api_key = os.getenv("OPENAI_API_KEY")
st.sidebar.text(f"OpenAI key set: {'Yes' if api_key else 'No'}")


# ----------------------------
#  USER INPUT (NO DEFAULTS)
# ----------------------------
st.markdown("### Enter Feature Values")

raw = {}
cols = st.columns(3)
i = 0

for feature in FEATURE_ORDER:
    with cols[i % 3]:
        # ask number input without defaults
        raw[feature] = [st.number_input(feature, value=0.0)]
    i += 1
    
    
# ----------------------------
#  RUN PIPELINE
# ----------------------------
if st.button("Run pipeline"):
    if not os.path.exists(PICKLE_PATH):
        st.error(f"Model not found at {PICKLE_PATH}. Run the dummy model creation script.")
    else:
        predictor = PredictorAgent(PICKLE_PATH, FEATURE_ORDER)
        strategy_agent = StrategyAgent()
        
        orchestrator = Orchestrator(predictor, strategy_agent)
        
        
        with st.spinner("Running all agents..."):
            result = orchestrator.run_pipeline(raw)

        st.subheader("Prediction (Agent 1)")
        st.json(result["prediction"])
        
        st.subheader("Initial Strategy (Agent 2)")
        st.write(result)