# app.py
from flask import Flask, jsonify, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

app = Flask(__name__)

# Load and preprocess the dataset
def load_data():
    # Assuming data.csv is your dataset file
    data = pd.read_csv('data.csv')
    data['Price'] = data['Price'].fillna(data['Price'].median())
    features = data[['Sweet', 'Acid', 'Color', 'Texture']]
    target = data['Overall']
    return train_test_split(features, target, test_size=0.2, random_state=42)

X_train, X_test, y_train, y_test = load_data()
model = LinearRegression()
model.fit(X_train, y_train)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return jsonify({'mse': mse, 'r2': r2})

if __name__ == '__main__':
    app.run(debug=True)
