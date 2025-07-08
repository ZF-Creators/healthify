from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("backend/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    prediction = None
    user_input = ""
    
    if request.method == "POST":
        user_input = request.form["symptoms"]
        try:
            # Predict probabilities
            probs = model.predict_proba([user_input])[0]
            top_indices = probs.argsort()[-5:][::-1]
            classes = model.classes_
            prediction = [(classes[i], probs[i]) for i in top_indices if probs[i] > 0.01]
        except Exception as e:
            prediction = [("Error: " + str(e), 1.0)]

    return render_template("chatbot.html", prediction=prediction, user_input=user_input)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
