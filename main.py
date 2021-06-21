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

#home
@app.route('/', methods = ['POST'])
def index():
    return render_template("index.html")

#basic operations

@app.route('/basic_add', methods = ['POST'])
def basic_add():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(float, array_str))
    n = len(array)
    result = add(array,n)
    return str(result)

@app.route('/basic_subtract', methods = ['POST'])
def basic_subtract():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(float, array_str))
    n = len(array)
    result = subtract(array,n)
    return str(result)

@app.route('/basic_multiply', methods = ['POST'])
def basic_multiply():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(float, array_str))
    n = len(array)
    result = multiply(array,n)
    return str(result)

@app.route('/basic_divide', methods = ['POST'])
def basic_divide():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(float, array_str))
    n = len(array)
    result = divide(array,n)
    return str(result)

@app.route('/basic_square', methods = ['POST'])
def basic_square():
    num = float(request.json['num'])
    result = num**2
    return str(result)

@app.route('/basic_power', methods = ['POST'])
def basic_power():
    num1 = float(request.json['num1'])
    num2 = float(request.json['num2'])
    result = pow(num1,num2)
    return str(result)

@app.route('/basic_sqrt', methods = ['POST'])
def basic_sqrt():
    num = float(request.json['num'])
    result = sqrt(2)
    return str(result)

@app.route('/basic_root', methods = ['POST'])
def basic_root():
    num = float(request.json['num'])
    index = int(request.json['index'])
    result = pow(num1,1/index)
    return str(result)

@app.route('/basic_e', methods = ['POST'])
def basic_e():
    num = float(request.json['num'])
    result = pow(e,num)
    return str(result)

@app.route('/basic_exp', methods = ['POST'])
def basic_exp():
    num = float(request.json['num'])
    result = pow(10,num)
    return str(result)

@app.route('/basic_log_10', methods = ['POST'])
def basic_log_10():
    num = float(request.json['num'])
    result = log10(num)
    return str(result)

@app.route('/basic_log', methods = ['POST'])
def basic_log():
    num = float(request.json['num'])
    base = int(request.json['base'])
    result = log(num,base)
    return str(result)

@app.route('/basic_ln', methods = ['POST'])
def basic_ln():
    num = float(request.json['num'])
    result = log(e,num)
    return str(result)    

@app.route('/basic_factorial', methods = ['POST'])
def basic_factorial():
    number = int(request.json['number'])
    result = factorial(number)
    return str(result)


@app.route('/basic_permutation', methods = ['POST'])
def basic_permutation():
    n = int(request.json['n'])
    r = int(request.json['r'])
    result = permutation(n,r)
    return str(result)

@app.route('/basic_combination', methods = ['POST'])
def basic_combination():    
    n = int(request.json['n'])
    r = int(request.json['r'])
    result = combination(n,r)
    return str(result)

@app.route('/basic_mean', methods = ['POST'])
def basic_mean():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)
    result = mean(array,n)
    return str(result)

@app.route('/basic_median', methods = ['POST'])
def basic_median():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)
    result = median(array,n)
    return str(result)

@app.route('/basic_mode', methods = ['POST'])
def basic_mode():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)
    result = mode(array)
    return str(result)

@app.route('/basic_min', methods = ['POST'])
def basic_min():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)
    result = minimum(array,n)
    return str(result)

@app.route('/basic_max', methods = ['POST'])
def basic_max():
    numbers = request.json['numbers']
    array_str = numbers.split(",")
    array = list(map(int, array_str))
    n = len(array)
    result = maximum(array,n)
    return str(result)

#trigonometric functions with degrees mode

@app.route('/trig_deg_sin', methods = ['POST'])
def trig_deg_sin():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(sin(angle),2)
    return str(ans)

@app.route('/trig_deg_cos', methods = ['POST'])
def trig_deg_cos():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(cos(angle),2)
    return str(ans)

@app.route('/trig_deg_tan', methods = ['POST'])
def trig_deg_tan():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(tan(angle),2)
    return str(ans)

@app.route('/trig_deg_cosec', methods = ['POST'])
def trig_deg_cosec():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(cosec(angle),2)
    return str(ans)

@app.route('/trig_deg_sec', methods = ['POST'])
def trig_deg_sec():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(sec(angle),2)
    return str(ans)

@app.route('/trig_deg_cot', methods = ['POST'])
def trig_deg_cot():
    angle = request.json['angle']
    angle = radians(float(angle))
    ans = round(cot(angle),2)
    return str(ans)

#trigonometric functions with radians mode

@app.route('/trig_rad_sin', methods = ['POST'])
def trig_rad_sin():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(sin(angle),2)
    return str(ans)

@app.route('/trig_rad_cos', methods = ['POST'])
def trig_rad_cos():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(cos(angle),2)
    return str(ans)

@app.route('/trig_rad_tan', methods = ['POST'])
def trig_rad_tan():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(tan(angle),2)
    return str(ans)

@app.route('/trig_rad_cosec', methods = ['POST'])
def trig_rad_cosec():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(cosec(angle),2)
    return str(ans)

@app.route('/trig_rad_sec', methods = ['POST'])
def trig_rad_sec():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(sec(angle),2)
    return str(ans)

@app.route('/trig_rad_cot', methods = ['POST'])
def trig_rad_cot():
    angle = request.json['angle']
    angle = degrees(float(angle))
    ans = round(cot(angle),2)
    return str(ans)

#inverse trigonometric functions with degrees mode

@app.route('/inv_trig_deg_arcsin', methods = ['POST'])
def inv_trig_deg_arcsin():
    number = request.json['number']
    number = float(number)
    ans = round(rad(asin(number)),2)

    if number == 1 or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 0.866 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 0.7071 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 0.5 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == 0 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)

@app.route('/inv_trig_deg_arccos', methods = ['POST'])
def inv_trig_deg_arccos():
    number = request.json['number']
    number = float(number)
    ans = round(rad(acos(number)),2)

    if number == 0 or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 0.5 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 0.7071 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 0.866 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == 1 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)

@app.route('/inv_trig_deg_arctan', methods = ['POST'])
def inv_trig_deg_arctan():
    number = request.json['number']
    number = float(number)
    ans = round(rad(atan(number)),2)

    if number == inf or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 1.732 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 1 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 0.577 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == 0 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)


@app.route('/inv_trig_deg_arccosec', methods = ['POST'])
def inv_trig_deg_arccosec():
    number = request.json['number']
    number = float(number)
    ans = round(rad(acosec(number)),2)

    if number == 1 or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 1.155 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 1.414 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 2 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == inf or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)

@app.route('/inv_trig_deg_arcsec', methods = ['POST'])
def inv_trig_deg_arcsec():
    number = request.json['number']
    number = float(number)
    ans = round(rad(asec(number)),2)

    if number == inf or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 2 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 1.414 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 1.155 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == 1 or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)

@app.route('/inv_trig_deg_arccot', methods = ['POST'])
def inv_trig_deg_arccot():
    number = request.json['number']
    number = float(number)
    ans = round(rad(acot(number)),2)

    if number == 0 or isclose(90,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 90

    if number == 0.577 or isclose(60,ans,rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 60

    if number == 1 or isclose(45,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 45

    if number == 1.732 or isclose(30,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 30

    if number == inf or isclose(0,rad(ans),rel_tol=1e-5,abs_tol=0.1)==True:
        ans = 0

    else:
        ans = ans

    return str(ans)

#inverse trigonometric functions with radians mode

@app.route('/inv_trig_rad_arcsin', methods = ['POST'])
def inv_trig_rad_arcsin():
    number = request.json['number']
    number = float(number)
    ans = round(asin(number),2)
    return str(ans)

@app.route('/inv_trig_rad_arccos', methods = ['POST'])
def inv_trig_rad_arccos():
    number = request.json['number']
    number = float(number)
    ans = round(acos(number),2)
    return str(ans)

@app.route('/inv_trig_rad_arctan', methods = ['POST'])
def inv_trig_rad_arctan():
    number = request.json['number']
    number = float(number)
    ans = round(atan(number),2)
    return str(ans)

@app.route('/inv_trig_rad_arccosec', methods = ['POST'])
def inv_trig_rad_arccosec():
    number = request.json['number']
    number = float(number)
    ans = round(acosec(number),2)
    return str(ans)

@app.route('/inv_trig_rad_arcsec', methods = ['POST'])
def inv_trig_rad_arcsec():
    number = request.json['number']
    number = float(number)
    ans = round(asec(number),2)
    return str(ans)

@app.route('/inv_trig_rad_arccot', methods = ['POST'])
def inv_trig_rad_arccot():
    number = request.json['number']
    number = float(number)
    ans = round(acot(number),2)
    return str(ans)

#hyperbolic functions
@app.route('/hyp_sinh', methods = ['POST'])
def hyp_sinh():
    number = request.json['number']
    number = float(number)
    ans = round(sinh(number),2)
    return str(ans)

@app.route('/hyp_cosh', methods = ['POST'])
def hyp_cosh():
    number = request.json['number']
    number = float(number)
    ans = round(cosh(number),2)
    return str(ans)

@app.route('/hyp_tanh', methods = ['POST'])
def hyp_tanh():
    number = request.json['number']
    number = float(number)
    ans = round(tanh(number),2)
    return str(ans)

@app.route('/hyp_cosech', methods = ['POST'])
def hyp_cosech():
    number = request.json['number']
    number = float(number)
    ans = round(cosech(number),2)
    return str(ans)

@app.route('/hyp_sech', methods = ['POST'])
def hyp_sech():
    number = request.json['number']
    number = float(number)
    ans = round(sech(number),2)
    return str(ans)

@app.route('/hyp_coth', methods = ['POST'])
def hyp_coth():
    number = request.json['number']
    number = float(number)
    ans = round(coth(number),2)
    return str(ans)

# inverse hyperbolic functions
@app.route('/inv_hyp_asinh', methods = ['POST'])
def inv_hyp_asinh():
    number = request.json['number']
    number = float(number)
    ans = round(asinh(number),2)
    return str(ans)

@app.route('/inv_hyp_acosh', methods = ['POST'])
def inv_hyp_acosh():
    number = request.json['number']
    number = float(number)
    ans = round(acosh(number),2)
    return str(ans)

@app.route('/inv_hyp_atanh', methods = ['POST'])
def inv_hyp_atanh():
    number = request.json['number']
    number = float(number)
    ans = round(atanh(number),2)
    return str(ans)

@app.route('/inv_hyp_acosech', methods = ['POST'])
def inv_hyp_acosech():
    number = request.json['number']
    number = float(number)
    ans = round(acosech(number),2)
    return str(ans)

@app.route('/inv_hyp_asech', methods = ['POST'])
def inv_hyp_asech():
    number = request.json['number']
    number = float(number)
    ans = round(asech(number),2)
    return str(ans)

@app.route('/inv_hyp_acoth', methods = ['POST'])
def inv_hyp_acoth():
    number = request.json['number']
    number = float(number)
    ans = round(acoth(number),2)
    return str(ans)


#conversion operations
#number systems
@app.route('/bin_to_dec', methods = ['POST'])
def bin_to_dec():
    number = request.json['number']
    ans = int(number,2)
    return str(ans)

@app.route('/bin_to_oct', methods = ['POST'])
def bin_to_oct():
    number = request.json['number']
    ans = oct(int(number,2))[2:]
    return str(ans)

@app.route('/bin_to_hex', methods = ['POST'])
def bin_to_hex():
    number = request.json['number']
    ans = hex(int(number,2))[2:]
    return str(ans)

@app.route('/dec_to_bin', methods = ['POST'])
def dec_to_bin():
    number = int(request.json['number'])
    ans = bin(number)[2:]
    return str(ans)

@app.route('/dec_to_oct', methods = ['POST'])
def dec_to_oct():
    number = int(request.json['number'])
    ans = oct(number)[2:]
    return str(ans)

@app.route('/dec_to_hex', methods = ['POST'])
def dec_to_hex():
    number = int(request.json['number'])
    ans = hex(number)[2:]
    return str(ans)

@app.route('/oct_to_bin', methods = ['POST'])
def oct_to_bin():
    number = int(request.json['number'], 8)
    ans = bin(number)[2:]
    return str(ans)

@app.route('/oct_to_dec', methods = ['POST'])
def oct_to_dec():
    number = request.json['number']
    ans = int(number,8)
    return str(ans)

@app.route('/oct_to_hex', methods = ['POST'])
def oct_to_hex():
    number = int(request.json['number'], 8)
    ans = hex(number)[2:]
    return str(ans)

@app.route('/hex_to_bin', methods = ['POST'])
def hex_to_bin():
    number = request.json['number']
    ans = bin(int(number,16))[2:]
    return str(ans)

@app.route('/hex_to_dec', methods = ['POST'])
def hex_to_dec():
    number = request.json['number']
    ans = int(number,16)
    return str(ans)

@app.route('/hex_to_oct', methods = ['POST'])
def hex_to_oct():
    number = request.json['number']
    ans = oct(int(number,16))[2:]
    return str(ans)

# temperature conversions
#kelvin to others
@app.route('/kelvin_to_celsius', methods = ['POST'])
def kelvin_to_celsius():
    temp = float(request.json['temp'])
    ans = temp - 273.15
    return str(ans)

@app.route('/kelvin_to_fahrenheit', methods = ['POST'])
def kelvin_to_fahrenheit():
    temp = float(request.json['temp'])
    ans = (temp - 273.15)*(9/5) + 32
    return str(ans)

@app.route('/kelvin_to_rankine', methods = ['POST'])
def kelvin_to_rankine():
    temp = float(request.json['temp'])
    ans = temp*(5/9)
    return str(ans)

@app.route('/kelvin_to_reaumur', methods = ['POST'])
def kelvin_to_reaumur():
    temp = float(request.json['temp'])
    ans = (temp - 273.15)*0.8
    return str(ans)

#celcius to others
@app.route('/celsius_to_kelvin', methods = ['POST'])
def celsius_to_kelvin():
    temp = float(request.json['temp'])
    ans = temp + 273.15
    return str(ans)

@app.route('/celsius_to_fahrenheit', methods = ['POST'])
def celsius_to_fahrenheit():
    temp = float(request.json['temp'])
    ans = (temp)*(9/5) + 32
    return str(ans)

@app.route('/celsius_to_rankine', methods = ['POST'])
def celsius_to_rankine():
    temp = float(request.json['temp'])
    ans = (temp + 273.15)*(9/5)
    return str(ans)

@app.route('/celsius_to_reaumur', methods = ['POST'])
def celsius_to_reaumur():
    ans = temp*0.8
    return str(ans)

#fahrenheit to others
@app.route('/fahrenheit_to_kelvin', methods = ['POST'])
def fahrenheit_to_kelvin():
    ans = (temp + 459.65)*(5/9)
    return str(ans)

@app.route('/fahrenheit_to_celsius', methods = ['POST'])
def fahrenheit_to_celcius():
    temp = float(request.json['temp'])
    ans = (temp-32)*(5/9)
    return str(ans)

@app.route('/fahrenheit_to_rankine', methods = ['POST'])
def fahrenheit_to_rankine():
    temp = float(request.json['temp'])
    ans = temp + 459.67
    return str(ans)

@app.route('/fahrenheit_to_reaumur', methods = ['POST'])
def fahrenheit_to_reaumur():
    temp = float(request.json['temp'])
    ans = (temp - 32)*(4/9)
    return str(ans)

#rankine to others
@app.route('/rankine_to_kelvin', methods = ['POST'])
def rankine_to_kelvin():
    temp = float(request.json['temp'])
    ans = temp*(5/9)
    return str(ans)

@app.route('/rankine_to_celsius', methods = ['POST'])
def rankine_to_celcius():
    temp = float(request.json['temp'])
    ans = (temp - 491.67)*(5/9)
    return str(ans)

@app.route('/rankine_to_fahrenheit', methods = ['POST'])
def rankine_to_fahrenheit():
    temp = float(request.json['temp'])
    ans = temp - 459.67
    return str(ans)

@app.route('/rankine_to_reaumur', methods = ['POST'])
def rankine_to_reaumur():
    temp = float(request.json['temp'])
    ans = (temp - 491.67)*(4/9)
    return str(ans)

#reaumur to others
@app.route('/reaumur_to_kelvin', methods = ['POST'])
def reaumur_to_kelvin():
    temp = float(request.json['temp'])
    ans = (temp)*(5/4) + 273.15
    return str(ans)

@app.route('/reaumur_to_celsius', methods = ['POST'])
def reaumur_to_celcius():
    temp = float(request.json['temp'])
    ans = (temp)/0.8
    return str(ans)

@app.route('/reaumur_to_fahrenheit', methods = ['POST'])
def reaumur_to_fahrenheit():
    temp = float(request.json['temp'])
    ans = temp*(9/4) + 32
    return str(ans)

@app.route('/reaumur_to_rankine', methods = ['POST'])
def reaumur_to_rankine():
    temp = float(request.json['temp'])
    ans = (temp)*(9/4) + 491.67
    return str(ans)


#angle conversion
@app.route('/deg_to_rad', methods = ['POST'])
def deg_to_rad():
    angle = float(request.json['angle'])
    ans = round(degrees(angle),2)
    return str(ans)

@app.route('/rad_to_deg', methods = ['POST'])
def rad_to_deg():
    angle = float(request.json['angle'])
    ans = round(radians(angle),2)
    return str(ans)


        
if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 3000, debug = True)