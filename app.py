from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

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


@app.route("/api/statistics")
def list_stat():
  return jsonify(X)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
