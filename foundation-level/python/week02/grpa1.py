"""
Accept three positive integers as input and check if they form the sides of a right triangle. 
Print YES if they form one, and NO if they do not. The input will have three lines, with one integer on each line. 
The output should be a single line containing one of these two strings: YES or NO.
"""


# DEBUG THE CODE
x = int(input())
y = int(input())
z = int(input())

if (x>0 and y>0 and z>0) and ((x ** 2 + y ** 2 == z ** 2) or (y ** 2 + z ** 2 == x ** 2) or (z ** 2 + x ** 2 == y ** 2)):
    print("YES")
else:
    print("NO")