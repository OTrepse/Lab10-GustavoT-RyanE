"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

#comment


import math

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return b/a
    except ZeroDivisionError:
        raise ZeroDivisionError
def logarithm(a,b):
    try:
        return math.log(a,b)
    except ValueError:





def exponent(a,b):