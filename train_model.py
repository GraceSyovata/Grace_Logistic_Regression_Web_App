from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Collect input values from the form
    input_data = [float(request.form[f'feature{i}']) for i in range(1, 31)]
    
    # Convert input data to numpy array and reshape
    input_data = np.array(input_data).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Prepare output message
    output_message = 'Predicted Diagnosis: Malignant' if prediction[0] else 'Predicted Diagnosis: Benign'
    
    return render_template('index.html', prediction_text=output_message)

if __name__ == '__main__':
    app.run(debug=True, port=4000)