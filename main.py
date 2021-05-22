from math import *
from sympy import *
from string import *
from itertools import *
from time import *
import os
from flask import Flask,request,render_template,url_for

template_dir = os.path.abspath('/home/manuel/Desktop/project/calculator_with_ui/views')
app = Flask(__name__, template_folder = template_dir)

@app.route('/', methods = 'POST')
def index():
    return render_template("index.html")

@app.route('/basic_operations', methods = 'POST')
def basic_operations():
    return None

@app.route('/trigonometric_operations', methods = 'POST')
def trigonometric_operations():
    return None

@app.route('/hyperbolic_operations', methods = 'POST')
def hyperbolic_operations():
    return None

@app.route('/conversion_operations')
def conversion_operations():
    return None  

        
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 8080, debug = True)