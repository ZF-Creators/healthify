# backend/symptom_checker.py

disease_symptoms = {
    "fever": ["Flu", "Malaria", "COVID-19"],
    "cough": ["Common Cold", "Bronchitis", "COVID-19"],
    "sore throat": ["Strep Throat", "Common Cold"],
    "headache": ["Migraine", "Tension Headache"],
    "fatigue": ["Anemia", "Thyroid Issues", "Depression"],
    "vomiting": ["Food Poisoning", "Stomach Flu"],
    "diarrhea": ["Cholera", "Food Poisoning"],
    "nausea": ["Pregnancy", "Food Poisoning"],
    "rash": ["Allergy", "Measles"],
    "runny nose": ["Cold", "Allergy"],
    "chills": ["Malaria", "Flu"],
    "body pain": ["Flu", "COVID-19"]
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
