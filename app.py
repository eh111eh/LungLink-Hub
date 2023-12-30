from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


# Function to load comments from the database
def load_comments_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM comments"))
    comments = [dict(zip(result.keys(), row)) for row in result.all()]
    return comments


# Function to save a new comment to the database
def save_comment_to_db(comment):
  with engine.connect() as conn:
    conn.execute(text("INSERT INTO comments (comment) VALUES (:comment)"),
                 comment=comment)


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


@app.route("/api/statistics")
def list_stat():
  return jsonify(X)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
