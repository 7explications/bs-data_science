"""
Accept two positive integers x and y as input. Print the number of digits in xy. You should be able to solve this problem using the concepts covered in week-1
"""

import os
os.system("cls")

x=int(input())
y=int(input())
s=str(x**y)
print(len(s))