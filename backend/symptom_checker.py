import joblib
import os

# Ensure the model path is correct regardless of where it's run from
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load the trained pipeline (TF-IDF + Logistic Regression)
model = joblib.load(MODEL_PATH)

def predict_disease(symptom_text):
    """
    Predicts the disease based on a string of symptoms entered by the user.

    Parameters:
    - symptom_text (str): A free-text description or list of symptoms

    Returns:
    - str: Predicted disease label
    """
    prediction = model.predict([symptom_text])
    return prediction[0]
