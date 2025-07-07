from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Expanded dataset (simplified for now)
data = {
    'fever': [1, 1, 0, 0, 1, 0],
    'cough': [1, 0, 1, 0, 1, 0],
    'headache': [0, 1, 1, 0, 1, 1],
    'fatigue': [1, 1, 0, 0, 1, 1],
    'sore_throat': [1, 0, 0, 0, 1, 0],
    'runny_nose': [1, 0, 1, 0, 0, 0],
    'nausea': [0, 1, 0, 0, 0, 1],
    'body_ache': [1, 1, 0, 0, 1, 1],
    'diarrhea': [0, 0, 0, 1, 0, 1],
    'disease': ['Flu', 'Migraine', 'Cold', 'Food Poisoning', 'COVID-19', 'Dengue']
}

df = pd.DataFrame(data)
X = df.drop('disease', axis=1)
y = df['disease']

model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptom_input):
    symptom_list = list(X.columns)
    input_data = [[1 if symptom in symptom_input else 0 for symptom in symptom_list]]
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    return prediction, dict(zip(model.classes_, [round(p * 100, 2) for p in probabilities]))
