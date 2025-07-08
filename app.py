from flask import Flask, render_template, request
from backend.symptom_checker import predict_disease

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_diagnosis', methods=['POST'])
def get_diagnosis():
    symptoms = request.form.get('symptoms')
    
    # If you're receiving comma-separated text: "fever, cough"
    symptom_list = [s.strip() for s in symptoms.split(',')]
    
    result, probabilities = predict_disease(symptom_list)
    
    # Format the result nicely for chatbot output
    response = f"Based on your symptoms, I suspect:\n"
    for disease, prob in probabilities.items():
        response += f"• {disease} ({prob}%)\n"
    
    return response.strip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)