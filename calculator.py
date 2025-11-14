# https://github.com/Lauren-Johnson44/lab11-LJ-RT.git
# Partner 1: Lauren Johnson
# Partner 2: Re'Niyah Tape

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        try:
            math.sqrt(a)
        except ValueError:
            return a
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        try:
            b / a
        except ZeroDivisionError:
            return a, b
    return b / a

def logarithm(a, b):
    if b <= 0:
        try:
            math.log(b, a)
        except ValueError:
            return a, b
    return math.log(b, a)

def exp(a, b):
    return a ** b