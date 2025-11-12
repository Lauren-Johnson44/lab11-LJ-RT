"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):

    try:
        return b / a
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
        return None


def log(a, b):
    if b <= 0:
        try:
            math.log(b, a)
        except ValueError:
            print("Error: Value cannot be less than or equal zero.")

    return math.log(b, a)

def exp(a, b):
    return a ** b








