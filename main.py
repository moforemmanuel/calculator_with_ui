from math import *
from sympy import *
from string import *
from itertools import *
from time import *
import os
from flask import Flask,request,render_template,url_for
from calculator import add

template_dir = os.path.abspath('/home/manuel/Desktop/project/calculator_with_ui/views')
app = Flask(__name__, template_folder = template_dir)

@app.route('/', methods = ['POST'])
def index():
    return render_template("index.html")

@app.route('/basic_operations', methods = ['GET','POST'])
def basic_operations():
    """n = request.args.get('n', 0, type = int)
    array = []
    for i in range(int(n)):
        print(f"Enter number {i+1} : ")
        item = request.args.get('item', None, type = int)
        array.append(item)"""
    items = request.args.get('items',None,type = str)
    array = items.split(" ")
    array = list(map(lambda x:int(x),array))
    n = len(array)
    add(array,n)

    return str(array,n)
        

    

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
    app.run(host = '127.0.0.1', port = 8080, debug = True)