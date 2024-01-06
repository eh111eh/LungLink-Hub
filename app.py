from flask import Flask, render_template, jsonify, request
from database import engine
from sqlalchemy import text
import logging

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

@app.route("/")
def hello_hacks():
    X, _, _ = load_data_from_db()
    return render_template('home.html', jobs=X)

@app.route('/statistics')
def statistics():
  X, _, _ = load_data_from_db()
  return render_template('stat.html', X=X)


@app.route('/area')
def area():
  X, _, _ = load_data_from_db()
  return render_template('area.html', X=X)


@app.route('/ml')
def ml():
  X, _, _ = load_data_from_db()
  return render_template('ml.html', X=X)


@app.route('/community')
def community():
  X, _, _ = load_data_from_db()
  return render_template('community.html', X=X)


@app.route("/api/statistics")
def list_stat():
  return jsonify(X)


@app.route("/api/area")
def list_area():
  return jsonify(X)


@app.route("/api/ml")
def list_ml():
  return jsonify(X)


@app.route("/api/community")
def list_community():
  return jsonify(X)

@app.route('/')
def index():
    return render_template('your_html_file.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)