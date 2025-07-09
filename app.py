from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# ✅ Load the entire pipeline (vectorizer + model)
model = joblib.load("backend/model.pkl")

# 🔍 TEST THE MODEL IMMEDIATELY AFTER LOADING
print("✅ Model loaded. Testing prediction...")

try:
    test_output = model.predict(["fever and headache"])
    print("✅ Model test prediction successful! Output:", test_output)
except Exception as e:
    print("❌ Error while testing model prediction:", e)

# Symptom list (optional for matching text)
symptom_list = [
    "fever", "cough", "sore throat", "headache", "fatigue", "vomiting",
    "diarrhea", "nausea", "rash", "runny nose", "chills", "body pain"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()
        user_msg = data.get("message", "")

        if not user_msg:
            return jsonify({"error": "Empty message"})

        try:
            # Match symptoms from input
            msg_lower = user_msg.lower()
            matched = [s for s in symptom_list if s in msg_lower]

            # Use the model directly
            probs = model.predict_proba([user_msg])[0]
            top_indices = np.argsort(probs)[-3:][::-1]
            top_preds = [(model.classes_[i], float(probs[i])) for i in top_indices]

            return jsonify({
                "matched": matched,
                "predictions": top_preds
            })

        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify({"error": f"❌ {str(e)}"})

    return render_template("chatbot.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
