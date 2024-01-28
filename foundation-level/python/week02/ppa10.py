"""
Accept a real number x as input and print the greatest integer less than or equal to x on the first line, followed by the smallest integer greater than or equal to x on the second line.
"""

import math
x=float(input())
floor_x = math.floor(x)
ceil_x = math.ceil(x)

print(floor_x)
print(ceil_x)