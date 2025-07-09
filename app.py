from flask import Flask, render_template, request, jsonify
import os
from backend.symptom_checker import disease_symptoms  # 👈 import rule-based map

app = Flask(__name__)

# Flat list of all known symptoms from disease_symptoms keys
symptom_list = list(set(
    s for symptoms in disease_symptoms.values() for s in symptoms
))

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

        # Score diseases based on symptom matches
        scored = []
        for disease, symptoms in disease_symptoms.items():
            if not symptoms:
                continue
            match_count = len(set(matched) & set(symptoms))
            if match_count > 0:
                percentage = round((match_count / len(symptoms)) * 100, 2)
                scored.append((disease, percentage))

        # Sort top 3 diseases
        scored.sort(key=lambda x: x[1], reverse=True)
        top_preds = scored[:3] if scored else [("No strong match found", 0)]

        return jsonify({
            "matched": matched,
            "predictions": top_preds
        })

    return render_template("chatbot.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
