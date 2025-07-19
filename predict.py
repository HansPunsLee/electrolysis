import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

print("Looking for model at:", os.path.join(MODEL_DIR, "cathode_model.pkl"))
print("Contents of model folder:", os.listdir(MODEL_DIR))


# Dynamically determine the absolute path to the models directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Load models and encoders safely using absolute paths
cathode_clf = joblib.load(os.path.join(MODELS_DIR, "cathode_model.pkl"))
anode_clf = joblib.load(os.path.join(MODELS_DIR, "anode_model.pkl"))
feature_encoders = joblib.load(os.path.join(MODELS_DIR, "feature_encoders.pkl"))
le_cathode = joblib.load(os.path.join(MODELS_DIR, "label_encoder_cathode.pkl"))
le_anode = joblib.load(os.path.join(MODELS_DIR, "label_encoder_anode.pkl"))

def preprocess_input(data_dict):
    """
    data_dict: dict with keys ['cation', 'anion', 'concentration', 'electrode_type', 'state']
    Returns: DataFrame with encoded features ready for prediction
    """
    df = pd.DataFrame([data_dict])

    for col, le in feature_encoders.items():
        if col in df.columns:
            df[col] = le.transform(df[col])

    return df

def predict_products(input_features):
    """
    input_features: dict with keys as above
    Returns: tuple (cathode_product, anode_product)
    """
    X = preprocess_input(input_features)

    cathode_pred_encoded = cathode_clf.predict(X)[0]
    anode_pred_encoded = anode_clf.predict(X)[0]

    cathode_product = le_cathode.inverse_transform([cathode_pred_encoded])[0]
    anode_product = le_anode.inverse_transform([anode_pred_encoded])[0]

    return cathode_product, anode_product


if __name__ == "__main__":
    # Example usage
    sample_input = {
        "cation": "Cu²⁺",
        "anion": "SO₄²⁻",
        "concentration": "high",
        "electrode_type": "inert",
        "state": "aqueous"
    }

    cathode, anode = predict_products(sample_input)
    print(f"Cathode product: {cathode}")
    print(f"Anode product: {anode}")
