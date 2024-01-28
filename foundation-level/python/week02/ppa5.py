"""
Write a program to realize the equation of a line given 2 points (x1,y1) and (x2,y2) in 2D space. 
The input is in 5 lines where, the first, second, third, and fourth lines represent x1, y1, x2, and y2 respectively. 
The fifth line corresponds to x3, Determine y3 using the equation of a straight line as given below:
(x-x1)/(x2-x1) = (y-y1)/(y2-y1)

The output should be "Vertical Line" if the line is vertical. In other cases, the output should be 2 lined, where the first line is the value of y3 and the second line indicates whether the slope of the line is positive, negative or zero. Print "Positive Slope", "Negative Slope" or "Horizontal Line" accordingly.

Note that all inputs are to be processed as real numbers.
"""
import os
os.system("cls")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
if x2 - x1 == 0:
    print("Vertical Line")
else:
    y3 = ((x3 - x1) / (x2 - x1)) * (y2 - y1) + y1
    slope = (y2 - y1) / (x2 - x1)
    print(y3)
    if slope > 0:
        print("Positive Slope")
    elif slope < 0:
        print("Negative Slope")
    else:
        print("Horizontal Line")    