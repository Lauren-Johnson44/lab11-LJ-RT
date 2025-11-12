"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        try:
            b / a
        except ZeroDivisionError:
            print("Error: You cannot divide by zero!")
    return b / a

def log(a, b):
    if b <= 0:
        try:
            math.log(b, a)
        except ValueError:
            print("Error: you cannot take the log of zero or a negative number!")
    return math.log(b, a)

def exp(a, b):
    return a ** b