import joblib

# Load model and encoder
model = joblib.load("backend/model.pkl")
encoder = joblib.load("backend/symptom_encoder.pkl")

def predict_disease(symptom_list):
    # Convert user input to encoded format
    symptoms = [s.strip().lower() for s in symptom_list]
    input_vector = encoder.transform([symptoms])

    prediction = model.predict(input_vector)[0]
    proba = model.predict_proba(input_vector)

    # Top 3 predictions
    top_indices = proba[0].argsort()[-3:][::-1]
    diseases = model.classes_
    top_probs = {diseases[i]: round(proba[0][i]*100, 1) for i in top_indices}

    return prediction, top_probs
