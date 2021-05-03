from math import *
from sympy import *
from string import *
from itertools import *
from time import *

from flask import Flask,request,render_template,url_for

app = Flask(__name__)

@app.route('/')
def index():
    operation = request.args.get("","")
    if cel:
        fah = ctf(cel)
    else:
        fah = ""
    return render_template("index.html") + "Fahrenheit : " + fah

@app.route("/add")
def adding():
    a = request.args.get("a","")
    b = request.args.get("b","")
    sum = add(a,b)
    if sum:
        sum = add(a,b)
    else:
        sum = ""
    return render_template("index.html") + "SUM : " + sum
def add(a,b):
    return a + b

def ctf(cel):
    try:
        fah= round(float(cel)*9/5 + 32,3)
        return str(fah)
    except ValueError:
        return "Invalid input"
        
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 8080, debug = True)