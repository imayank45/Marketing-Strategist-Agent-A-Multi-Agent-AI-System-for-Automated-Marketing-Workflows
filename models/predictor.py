# models/predictor.py
import joblib
import pandas as pd
import os

class PredictorAgent:
    def __init__(self, pickle_path: str, feature_order: list):
        if not os.path.exists(pickle_path):
            raise FileNotFoundError(f"Pickle model not found at {pickle_path}")

        # Load using joblib - IMPORTANT FIX
        self.model = joblib.load(pickle_path)

        self.feature_order = feature_order

    def preprocess(self, raw: dict) -> pd.DataFrame:
        df = pd.DataFrame(raw)

        # ensure columns exist and in correct order
        for c in self.feature_order:
            if c not in df.columns:
                df[c] = 0
        df = df[self.feature_order]

        return df

    def predict(self, raw: dict) -> dict:
        df = self.preprocess(raw)

        try:
            proba = self.model.predict_proba(df)
            prob = float(proba[0][1])
        except Exception:
            pred = self.model.predict(df)
            prob = float(pred[0])

        return {
            "probability": prob,
            "decision": 1 if prob >= 0.5 else 0,
            "preprocessed": df.to_dict(orient="records")[0]
        }
