from math import *
from sympy import *
from string import *
from itertools import *
from time import *
import os
from flask import Flask,request,render_template,url_for


array = []
def nums(array,n):
	
	for i in range(n):
		print("Enter item ",i+1)
		item=int(input())
		array.append(item)
	if len(array)==1:
		print("number is  : ", array)
	elif len(array)>=2:
		print("numbers are : ",array)
	else:
		print("Error...\n")
		
def add(array,n):
	sum = 0
	if n>1:
		for i in range(n):
			sum+=array[i]
		return sum
	elif n == 1:
		return array[0]
	else:
		return "Error\n"
	
def subtract(array,n):
	diff = array[0]
	if n>1:
		for i in range(1,n):
			diff-=array[i]
		return diff
	elif n == 1:
		return array[0]
	else:
		return "Error\n"
	
def multiply(array,n):
	mult = 1
	if n>1:
		for i in range(n):
			mult*=array[i]
		return mult
	elif n == 1:
		return array[0]
	else:
		return "Error\n"

def rad(ans):
	return (ans*180)/pi

def divide(array,n):
	
	div = 1
	if n>1:
		for i in range(n):
			div/=array[i]
		return div
	elif n == 1:
		return array
	else:
		return "Error\n"

	
		
	
	
def mean(array,size):
	sum=0
	for i in range(size):
		sum=sum+array[i]
		i+=1
	av=(sum)/size
	print("Mean is : ", av,  "\n")
	

def minimum(array,n):
		min=array[0]
		for i in range(1,n):
			if array[i]<min:
				min=array[i]
		print("Minimum element is : \n",min, "\n")
		
def maximum(array,n):
		max=array[0]
		for i in range(1,n):
			if array[i]>max:
				max=array[i]
		print("Maximum element is : \n",max,"\n")


def bubblesort(array,n):
		for i in range(n):
			for j in range(n-i-1):
				if array[j]>array[j+1] :
					temp = array[j]
					array[j] = array[j+1]
					array[j+1] = temp
		print("Sorted list is : ",array,"\n")

def median(array,n):
		bubblesort(array,n)
		middle = n/2
		if middle%2!=0:
			index = int(middle)
			print("Median is : ",array[index],"\n")
		else :
			half=int(middle)
			med=(array[half]+array[half-1])/2
			print("Median is : ",med,"\n")
			
			
def mode(input):
    counter = 2
    num = []

    for i in input:
        currentCounter = input.count(i);
        if(currentCounter >= counter):
            counter = currentCounter
            num.append(i)
    
    if(num == input):
        return "no mod found"

    num = list(set(num))

    if(len(num) < 1):
        return "no mod found"
    
    if(len(num)==1):
        	print("Mode is : ",num,"\n")
    
    if(len(num)>1):
    		print("Modes are : ",num,"\n")

out = None


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
    items = request.args.get('items',"1",type = str)
    #items = request.form['items']
    array = items.split(" ")
    array = list(map(lambda x:int(x),array))
    n = len(array)

    # print("""Choose a Basic Operation : 
	# 		1)   Addition
	# 		2)  Subtraction
	# 		3) Multiplication
	# 		4) Division
	# 		5)  Power
	# 		6) logarithm
	# 		7)Mean
	# 		8)Median
	# 		9) Mode
	# 		10)  Minimum
	# 		11) Maximum 
	# 		12)Exit\n
    #         input : """)

    BC = request.args.get('BC',1,type=int)
    #BC = request.form['BC']
				
    if BC == 1: #addition
        #n = int(input("How many numbers do you wish to operate on? : \n"))
        #nums(array,n)
        #print("Sum is : ",add(array,n))
        global out
        out = add(array,n)
        return "Sum is " + str(out)
        #return render_template('index.html',out=out)
            
        
    if BC == 2: #subtraction
        #n = int(input("How many numbers do you wish to operate on? : \n"))
        #nums(array,n)
        #print("Difference is : ",subtract(array,n))
        out = subtract(array,n)
        return "Difference is " + str(out)
        #return render_template('index.html',out=out)
        
    if BC == 3:#Multiplication
        #n = int(input("How many numbers do you wish to operate on? : \n"))
        #nums(array,n)
        #print("Product is : ",multiply(array,n))
        out = multiply(array,n)
        return "Product is " + str(out)
    
    if BC == "iv":#Division
        n = int(input("How many numbers do you wish to operate on? : \n"))
        nums(array,n)
        print("Quotient is : ",divide(array,n))
        
        
    if BC == "v":#power
        a = float(input("Enter radix : "))
        b = float(input("Enter power : "))
        print("Answer is : ",pow(a,b))
    
    
    if BC == "vi":#log
        a = int(input("Input base : "))
        b = int(input("Input operand : "))
        print("Answer is : ",log(a,b))
        
    if BC == "vii":#mean
        n = int(input("Input list size : "))
        nums(array,n)
        mean(array,n)
        
    if BC == "viii":#median
        n = int(input("Input list size : "))
        nums(array,n)
        median(array,n)
        
    if BC == "ix":#mode
        n=int(input("Input list size : "))
        nums(array,n)
        mode(array)
        
    if BC == "x":#minimum
        n=int(input("Input list size : "))
        nums(array,n)
        minimum(array,n)
        
    if BC == "xi":#maximum
        n=int(input("Input list size : "))
        nums(array,n)
        maximum(array,n)
        
    if BC == "xii":#exit
        print("Exiting Basic Operations...\n")
        

    else:
        return None

    
   
        

    

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