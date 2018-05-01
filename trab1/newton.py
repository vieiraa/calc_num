import math, re
import numpy as np

def derivative(f, x, h=0.00001):
    d = (f(x+h)-f(x))/h
    return d

def newton(f, x0, h):
    i = 0
    last_x = x0
    next_x = x0

    while True:
        last_x = next_x
        next_x = last_x - f(last_x) / derivative(f, last_x, h)
        i += 1
        print("Iteração: ", i)
        print("Valor: ", next_x)
        if abs(last_x - next_x) < h:
            break

    return next_x

def func(x):
    return np.exp(-x) - x

print(newton(func, 5, 0.00001))
