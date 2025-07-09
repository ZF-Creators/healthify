# backend/symptom_checker.py

disease_symptoms = {
    "Viral Fever (Non-specific virus)": {
        "symptoms": ["fever", "body pain", "fatigue"],
        "score_range": (40, 50)
    },
    "Influenza (Flu)": {
        "symptoms": ["fever", "cough", "sore throat", "body pain"],
        "score_range": (20, 25)
    },
    "Dengue Fever": {
        "symptoms": ["fever", "rash", "headache", "vomiting"],
        "score_range": (10, 15)
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "sore throat", "body pain", "chills"],
        "score_range": (10, 15)
    },
    # Add more diseases here if needed
}

def match_symptoms(user_input):
    user_input = user_input.lower()
    matched_symptoms = [symptom for symptom in disease_symptoms if symptom in user_input]
    
    possible_diseases = set()
    for symptom in matched_symptoms:
        possible_diseases.update(disease_symptoms[symptom])

    return {
        "matched_symptoms": matched_symptoms,
        "possible_diseases": list(possible_diseases)
    }
