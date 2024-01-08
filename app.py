from flask import Flask, render_template, jsonify, request
from database import engine, load_data_from_db
from sqlalchemy import text
import logging
from database import load_data_from_db
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import numpy as np
import pandas as pd


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Function to load X, countries, and years from the database
def load_data_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM X"))
    X = [dict(zip(result.keys(), row)) for row in result.all()]

    result = conn.execute(text("SELECT DISTINCT country FROM X"))
    countries = [row[0] for row in result.all()]

    result = conn.execute(text("SELECT DISTINCT year FROM X"))
    years = [row[0] for row in result.all()]

  return X, countries, years

# Function to load Xy_withASR data from the database
def load_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Xy_withASR"))
        Xy_withASR = [dict(zip(result.keys(), row)) for row in result.all()]
    return Xy_withASR

# Split data into features and labels
Xy_withASR = load_data()

# Convert list of dictionaries to a pandas DataFrame
Xy_withASR_df = pd.DataFrame(Xy_withASR)

features = np.array(Xy_withASR_df[['c_dollar2_poverty', 'c_forest_area', 'c_health_expenditure', 'c_out_of_pocket', 'c_physician', 'c_tuberculosis', 'c_urban_pop']])
labels_female = np.array(Xy_withASR_df['ASR (female)'])
labels_male = np.array(Xy_withASR_df['ASR (male)'])

# Create AdaBoost regressor models
adaboost_female = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=10), n_estimators=150,
    learning_rate=0.5
)
adaboost_male = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=10), n_estimators=150,
    learning_rate=0.5
)

# Train the models
adaboost_female.fit(features, labels_female)
adaboost_male.fit(features, labels_male)

@app.route("/")
def hello_hacks():
    X, _, _ = load_data_from_db()
    return render_template('home.html', jobs=X)

@app.route('/statistics')
def statistics():
  X, _, _ = load_data_from_db()
  return render_template('stat.html', X=X)


@app.route('/area', methods=['GET', 'POST'])
def area():
  if request.method == 'POST':
    try:
      # Get user input from the form
        income = float(request.form['income'])
        forest_area = float(request.form['forest_area'])
        health_expenditure = float(request.form['health_expenditure'])
        out_of_pocket = float(request.form['out_of_pocket'])
        physician = float(request.form['physician'])
        tuberculosis = float(request.form['tuberculosis'])
        urban_pop = float(request.form['urban_pop'])

        # Make predictions using the trained model
        user_input = [income, forest_area, health_expenditure, out_of_pocket, physician, tuberculosis, urban_pop]
        predicted_female_mortality = adaboost_female.predict([user_input])[0]
        predicted_male_mortality = adaboost_male.predict([user_input])[0]

        # Return predictions and input features as JSON
        return jsonify({
            'input_features': {
                'income': income,
                'forest_area': forest_area,
                'health_expenditure': health_expenditure,
                'out_of_pocket': out_of_pocket,
                'physician': physician,
                'tuberculosis': tuberculosis,
                'urban_pop': urban_pop,
            },
            'predicted_female_mortality': predicted_female_mortality,
            'predicted_male_mortality': predicted_male_mortality
        })

    except Exception as e:
        # Handle errors, e.g., invalid input format
        return jsonify({'error': f'Error processing request: {str(e)}'}, 400)

  return render_template('area.html')


@app.route('/ml')
def ml():
  X, _, _ = load_data_from_db()
  return render_template('ml.html', X=X)


@app.route("/api/statistics")
def list_stat():
  return jsonify(X)


@app.route("/api/area")
def list_area():
  return jsonify(X)


@app.route("/api/ml")
def list_ml():
  return jsonify(X)

@app.route('/')
def index():
    return render_template('your_html_file.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
