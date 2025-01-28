from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

# Initializing the Flask app
app = Flask(__name__)

# Loading the trained model, encoder, and scaler
model = joblib.load('myproject/code/car_price_linear_regression_model.pkl')
encoder = joblib.load('myproject/code/onehotencoder.pkl')
scaler = joblib.load('myproject/code/scaler.pkl')

# Defining the categorical columns for encoding
categorical_columns = ['fuel', 'owner', 'brand']
numerical_columns = ['km_driven', 'seats', 'year']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the required attributes from the data
        fuel = request.form['fuel']
        owner = request.form['owner']
        brand = request.form['brand']
        km_driven = float(request.form['km_driven'])
        seats = int(request.form['seats'])
        year = int(request.form['year'])

        # Creating an input DataFrame
        categorical_data = [[fuel, owner, brand]]
        numerical_data = [[km_driven, seats, year]]

        # Encoding the categorical data
        encoded_categorical_data = encoder.transform(categorical_data)

        # Scaling the numerical data
        scaled_numerical_data = scaler.transform(numerical_data)

        # Combining the  categorical and numerical features
        input_data = np.hstack([scaled_numerical_data, encoded_categorical_data])

        # Predicting the car price 
        prediction = model.predict(input_data)[0]

        # Rendering the result.html with the predicted price
        return render_template('result.html', prediction=round(prediction, 2))
    
    except Exception as e:
        # Returning error message if something goes wrong(using exception)
        return render_template('index.html', error="Invalid input data. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
