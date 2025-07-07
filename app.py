from flask import Flask, render_template, request
from backend.symptom_checker import predict_disease

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    probabilities = None
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms')
        result, probabilities = predict_disease(symptoms)
    return render_template('index.html', result=result, probs=probabilities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
