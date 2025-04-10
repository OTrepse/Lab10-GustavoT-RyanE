"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/OTrepse/Lab10-GustavoT-RyanE
# Partner 1 = Gustavo Torres
# Partner 2 = Ryan Esperto

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ValueError
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
