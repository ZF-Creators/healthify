from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Dummy dataset
data = {
    'fever': [1, 1, 0, 0],
    'cough': [1, 0, 1, 0],
    'headache': [0, 1, 1, 0],
    'disease': ['Flu', 'Migraine', 'Cold', 'Healthy']
}

df = pd.DataFrame(data)
X = df.drop('disease', axis=1)
y = df['disease']

model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptom_input):
    input_data = [[1 if symptom in symptom_input else 0 for symptom in ['fever', 'cough', 'headache']]]
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    return prediction, dict(zip(model.classes_, [round(p*100, 2) for p in probabilities]))