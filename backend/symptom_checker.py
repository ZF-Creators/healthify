# backend/symptom_checker.py

disease_symptoms = {
    "Viral Fever": ["fever", "body pain", "fatigue"],
    "Flu": ["fever", "cough", "sore throat", "body pain"],
    "Dengue": ["fever", "rash", "headache", "vomiting"],
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
