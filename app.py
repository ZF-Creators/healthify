from flask import Flask, render_template, request
from backend.symptom_checker import predict_disease

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    user_input = ""
    
    if request.method == "POST":
        user_input = request.form.get("symptoms", "")
        if user_input.strip() != "":
            prediction = predict_disease(user_input)

    return render_template("index.html", prediction=prediction, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
