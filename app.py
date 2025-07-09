from flask import Flask, render_template, request, jsonify
from backend.symptom_checker import match_symptoms
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()
        user_msg = data.get("message", "").strip()

        if not user_msg:
            return jsonify({"error": "❌ Empty message"})

        try:
            result = match_symptoms(user_msg)

            if not result["matched_symptoms"]:
                return jsonify({
                    "matched": [],
                    "predictions": ["❌ No recognizable symptoms found."]
                })

            return jsonify({
                "matched": result["matched_symptoms"],
                "predictions": result["possible_diseases"]
            })

        except Exception as e:
            print(f"Error during processing: {e}")
            return jsonify({"error": f"❌ Internal error: {str(e)}"})

    return render_template("chatbot.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
