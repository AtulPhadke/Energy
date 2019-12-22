from flask import Flask
from flask import render_template, request
import time
import os
app = Flask(__name__)

@app.route('/')
def function():
    humidity = 0
    temperature = 2
    wateranalog = 3
    print ("something for testing")
    return render_template("Data.html", humidity=humidity, temperature=temperature, wateranalog=wateranalog)
