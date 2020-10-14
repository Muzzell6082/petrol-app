import requests
import json
import sqlite3
from flask import Flask, render_template


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Instantiate a Flask app
app = Flask(__name__)

with open('static/data.json') as stations:
    stations = json.load(stations)

# Route and render template
@app.route('/')
def index():
    return render_template('index.html', stations=stations)

# To extract the current temperature from the above call, simply access the JSON result
# current = data["current"]["dt"]
# print(current)
# 5.25

# The hourly forecast is stored under the key hourly
# – it is easy to iterate over the result set and extract the hour and temperature for each entry
# hourly = data["hourly"]

# for entry in hourly:
#    dt = datetime.fromtimestamp(entry["dt"], pytz.timezone('Europe/Vienna'))
#    temp = entry["temp"]
