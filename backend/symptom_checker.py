# backend/symptom_checker.py

disease_symptoms = {
    "Flu": ["fever", "chills", "body pain"],
    "Malaria": ["fever", "chills"],
    "COVID-19": ["fever", "cough", "body pain"],
    "Common Cold": ["cough", "sore throat", "runny nose"],
    "Bronchitis": ["cough"],
    "Strep Throat": ["sore throat"],
    "Migraine": ["headache"],
    "Tension Headache": ["headache"],
    "Anemia": ["fatigue"],
    "Thyroid Issues": ["fatigue"],
    "Depression": ["fatigue"],
    "Food Poisoning": ["vomiting", "diarrhea", "nausea"],
    "Stomach Flu": ["vomiting"],
    "Cholera": ["diarrhea"],
    "Pregnancy": ["nausea"],
    "Allergy": ["rash", "runny nose"],
    "Measles": ["rash"],
    "Cold": ["runny nose"]
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
