from math import *
from sympy import diff
import numpy as np

def derivada(f, x, h):
	d = (1.0/(2*h))*(f(x+h)-f(x-h))
	return d

def newton(f, x0, h):
	i = 0
	lastX = x0
	nextX = lastX + 10 * h
	
	while (abs(lastX - nextX) > h):
		newY = f(nextX)
		lastX = nextX
		nextX = lastX - newY / derivada(f, lastX, h)
		i += 1
		print (i)
		
	return nextX

def func(x):
	return np.exp(-x) - x

print(newton(func, 5, 0.001))
