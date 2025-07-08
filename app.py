from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("backend/model.pkl")
history = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global history
    user_input = ""
    if request.method == 'POST':
        user_input = request.form['symptoms']
        if user_input.strip():
            try:
                pred_probs = model.predict_proba([user_input])[0]
                classes = model.classes_
                top_preds = sorted(zip(classes, pred_probs), key=lambda x: x[1], reverse=True)[:5]
                response = "<br>".join([f"{disease}: {prob*100:.2f}%" for disease, prob in top_preds])
            except Exception as e:
                response = f"⚠️ Error: {str(e)}"
        else:
            response = "Please enter symptoms."

        history.append({"user": user_input, "response": response})

    return render_template("index.html", history=history)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
