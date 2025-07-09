from flask import Flask, render_template, request, jsonify
import os
from backend.symptom_checker import disease_symptoms  # 👈 import updated structure

app = Flask(__name__)

# Flat list of all known symptoms from the new structure
symptom_list = list(set(
    s for disease in disease_symptoms.values() for s in disease["symptoms"]
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

        # Score diseases based on symptom matches and fixed score range
        scored = []
        for disease, info in disease_symptoms.items():
            symptoms = info["symptoms"]
            score_range = info["score_range"]
            if not symptoms:
                continue

            match_count = len(set(matched) & set(symptoms))
            if match_count > 0:
                # Optional: Use average score instead of range
                avg_score = round((score_range[0] + score_range[1]) / 2, 1)
                scored.append((disease, avg_score))

        # Sort and pick top 3
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
