import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

os.makedirs("backend", exist_ok=True)

df = pd.read_csv("C:/Users/faraz/Downloads/Healthify/ml-training/disease_symptom_classifier.csv")

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and fit the pipeline
pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),  # this will now be fitted
    ("classifier", LogisticRegression(max_iter=200))
])
pipeline.fit(X_train, y_train)

# Save the entire pipeline (vectorizer + classifier)
joblib.dump(pipeline, "backend/model.pkl", compress=9)

print(f"✅ Model trained! Accuracy: {pipeline.score(X_test, y_test)*100:.2f}%")
