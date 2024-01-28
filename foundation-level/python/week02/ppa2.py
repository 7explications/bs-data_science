"""
Consider the piece-wise function given below.
f(x)=   x+ 2    0<x<10
        x2+2    10<=x
        0       otherwise  
"""
import os
os.system("cls")

x=float(input())
if x>0 and x<10:
    fx=x+2
elif x>=10:
    fx= (x**2)+2
else :
    fx=0.0
print(fx)    