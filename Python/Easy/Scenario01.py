import os

#Import the necessary packages


def sim_int(p,n,r): 
    p= int(input())
    n= int(input())
    r= int(input())
      
    si = (p * n * r) / 100
    
    print("The Simple Interest is {}".format(si))
    print(['n', 'p', 'r', 'si'])
    return si, ['n', 'p', 'r', 'si']
      

from math import floor, ceil

def ceil_floor(a,b):
    a= input()
    b= input()
    
    result = 0
    val = ""
    op = None
    for i in a:
        if((i == '+' or i == '-' or i == '*' or i == '/' or i == '%') and op is None):
            op = i
            if(result == 0):
                result = result + float(val)
                val = ""
        elif((i == '+' or i == '-' or i == '*' or i == '/' or i == '%') and op is not None):
            if(op == '+'):
                result = result + float(val)
                op = i
                val = ""
            elif(op == '-'):
                result = result - float(val)
                op = i
                val = ""
            elif(op == '*'):
                result = result * float(val)
                op = i
                val = ""
            elif(op == '/'):
                result = result / float(val)
                op = i
                val = ""
            elif(op == '%'):
                result = result % float(val)
                op = i
                val = ""
        else:
            val += i
            
    if(op == '+'):
        result = result + float(val)
        op = i
        val = ""
    elif(op == '-'):
        result = result - float(val)
        op = i
        val = ""
    elif(op == '*'):
        result = result * float(val)
        op = i
        val = ""
    elif(op == '/'):
        result = result / float(val)
        op = i
        val = ""
    elif(op == '%'):
        result = result % float(val)
        op = i
        val = ""
    
    a = ceil(result)
    
    result = 0
    val = ""
    op = None
    for i in b:
        if((i == '+' or i == '-' or i == '*' or i == '/' or i == '%') and op is None):
            op = i
            if(result == 0):
                result = result + float(val)
                val = ""
        elif((i == '+' or i == '-' or i == '*' or i == '/' or i == '%') and op is not None):
            if(op == '+'):
                result = result + float(val)
                op = i
                val = ""
            elif(op == '-'):
                result = result - float(val)
                op = i
                val = ""
            elif(op == '*'):
                result = result * float(val)
                op = i
                val = ""
            elif(op == '/'):
                result = result / float(val)
                op = i
                val = ""
            elif(op == '%'):
                result = result % float(val)
                op = i
                val = ""
        else:
            val += i
            
    if(op == '+'):
        result = result + float(val)
        op = i
        val = ""
    elif(op == '-'):
        result = result - float(val)
        op = i
        val = ""
    elif(op == '*'):
        result = result * float(val)
        op = i
        val = ""
    elif(op == '/'):
        result = result / float(val)
        op = i
        val = ""
    elif(op == '%'):
        result = result % float(val)
        op = i
        val = ""
    
    b = floor(result)
        
    print(a)
    print(b)
    
    return a,b

from math import sqrt
def lists():
    lst =  []
    for i in range(0, 5):
        val = int(input())
        lst.append(val)
    
    for i in range(0, 5):
        lst[i] = round(sqrt(lst[i]), 2)
    
    print(lst)
    print(type(lst[0]))
    return lst, type(lst[0])
# Driver code
p=0
n=0
r=0
si=sim_int(p,n,r) 
a=0
b=0
c=ceil_floor(a,b)
e=lists()