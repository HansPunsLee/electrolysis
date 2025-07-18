import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
DATA_PATH = "data/electrolytic_dataset.csv"

def preprocess_data(df):
    # Features to use
    feature_cols = ["cation", "anion", "concentration", "electrode_type", "state"]

    X = df[feature_cols].copy()
    y_cathode = df["cathode_product"]
    y_anode = df["anode_product"]

    # Encode categorical features
    encoders = {}
    for col in feature_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        encoders[col] = le

    # Encode targets separately
    le_cathode = LabelEncoder()
    y_cathode_enc = le_cathode.fit_transform(y_cathode)

    le_anode = LabelEncoder()
    y_anode_enc = le_anode.fit_transform(y_anode)

    return X, y_cathode_enc, y_anode_enc, encoders, le_cathode, le_anode

def train_and_save_models():
    df = pd.read_csv(DATA_PATH)

    X, y_cathode, y_anode, encoders, le_cathode, le_anode = preprocess_data(df)

    # Train-test split for evaluation (optional)
    X_train, X_test, y_cathode_train, y_cathode_test, y_anode_train, y_anode_test = train_test_split(
        X, y_cathode, y_anode, test_size=0.2, random_state=42
    )

    # Train classifiers
    cathode_clf = DecisionTreeClassifier(random_state=42)
    cathode_clf.fit(X_train, y_cathode_train)

    anode_clf = DecisionTreeClassifier(random_state=42)
    anode_clf.fit(X_train, y_anode_train)

    # Save models and encoders
    os.makedirs("models", exist_ok=True)
    joblib.dump(cathode_clf, "models/cathode_model.pkl")
    joblib.dump(anode_clf, "models/anode_model.pkl")
    joblib.dump(encoders, "models/feature_encoders.pkl")
    joblib.dump(le_cathode, "models/label_encoder_cathode.pkl")
    joblib.dump(le_anode, "models/label_encoder_anode.pkl")

    print("✅ Models and encoders saved to models/")

if __name__ == "__main__":
    train_and_save_models()
