from flask import Flask, render_template, jsonify

app = Flask(__name__)

DATA = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Korea',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'UK',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}]


@app.route("/")
def hello_hacks():
  return render_template('home.html')


@app.route("/api/data")
def list_data():
  return jsonify(DATA)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
