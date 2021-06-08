from math import *
from sympy import *
from string import *
from itertools import *
from time import *
import os
from flask import Flask,request,render_template,url_for
from calculator import *

template_dir = os.path.abspath('/home/manuel/Desktop/project/calculator_with_ui/views')
app = Flask(__name__, template_folder = template_dir)

@app.route('/', methods = ['POST'])
def index():
    return render_template("index.html")

@app.route('/basic_operations', methods = ['POST'])
def basic_operations():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)

    result = add(array, n)

    return str(result)

@app.route('/trigonometric_operations', methods = ['POST'])
def trigonometric_operations():
    return None

@app.route('/hyperbolic_operations', methods = ['POST'])
def hyperbolic_operations():
    return None

@app.route('/conversion_operations', methods = ['POST'])
def conversion_operations():
    return None  

        
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 3000, debug = True)