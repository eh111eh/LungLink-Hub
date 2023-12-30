from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_X_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from X"))
        X = []
        for row in result.all():
            X.append(dict(zip(result.keys(), row)))
        return X

@app.route("/")
def hello_hacks():
    X = load_X_from_db()
    return render_template('home.html', jobs=X)

@app.route('/statistics')
def statistics():
    X = load_X_from_db()
    return render_template('stat.html', X=X)


@app.route("/api/stat")
def list_stat():
  return jsonify(X)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
