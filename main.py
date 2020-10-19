import json
import sqlite3
from flask import Flask, render_template

# Instantiate a Flask app
app = Flask(__name__)

with open('static/data.json') as stations:
    stations = json.load(stations)

# Route and render template
@app.route('/')
def index():
    return render_template('index.html', stations=stations)
