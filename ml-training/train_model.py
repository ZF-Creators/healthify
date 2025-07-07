import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import joblib

# Load the dataset
df = pd.read_csv("dataset.csv")

# Convert string of symptoms to list
df['symptoms'] = df['symptoms'].apply(lambda x: [i.strip() for i in x.split(',')])

# Prepare symptom columns
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['symptoms'])

# Target variable
y = df['disease']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and symptom list
joblib.dump(model, "model.pkl")
joblib.dump(mlb, "symptom_encoder.pkl")

print("✅ Model trained and saved as model.pkl")
