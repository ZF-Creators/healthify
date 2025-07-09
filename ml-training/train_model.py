import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# ✅ Make sure backend folder exists
os.makedirs("backend", exist_ok=True)

# ✅ Load your dataset
df = pd.read_csv("C:/Users/faraz/Downloads/Healthify/ml-training/disease_symptom_classifier.csv")

# ✅ Check columns
if not {'label', 'text'}.issubset(df.columns):
    raise ValueError("The dataset must have 'label' and 'text' columns")

X = df['text']
y = df['label']

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Create pipeline (includes vectorizer)
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=200))
])
model.fit(X_train, y_train)

# ✅ Save only the model
joblib.dump(model, "backend/model.pkl", compress=9)

print(f"✅ Model trained! Accuracy: {model.score(X_test, y_test)*100:.2f}%")
