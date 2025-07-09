from flask import Flask, render_template, request, jsonify
import os
from backend.symptom_checker import disease_symptoms  # 👈 import rule-based map

app = Flask(__name__)

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
        user_msg = data.get("message", "").lower()

        if not user_msg:
            return jsonify({"error": "Empty message"})

        # Match symptoms
        matched = [s for s in symptom_list if s in user_msg]

        # Score diseases based on how many symptoms match
        scored = []
        for disease, symptoms in disease_symptoms.items():
            match_count = len(set(matched) & set(symptoms))
            score = match_count / len(symptoms)  # simple score %
            if match_count > 0:
                scored.append((disease, round(score * 100, 2)))

        # Sort diseases by score
        scored.sort(key=lambda x: x[1], reverse=True)
        top_preds = scored[:3]

        # ✅ Add fallback if no diseases matched
        if not top_preds:
            top_preds = [("No strong match found", 0)]

        return jsonify({
            "matched": matched,
            "predictions": top_preds
        })

    return render_template("chatbot.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
