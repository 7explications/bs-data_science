"""
a=10
b=12
c=13
x, y, z = a, b, c
x = y = z
print(x == y == z)
print(x == y == z==a)
print(x == y == z==b)
print(x == y == z==c)


a=2
b=3 
c=9
d=7
w= float(str(a)+"."+str(b)+str(c)+str(d))
x=float(w)
print(int(x))
print(int(-x))

alphabets = 'abcdefghijklmnopqrstuvwxyz'
even = alphabets[0: 10: 2]
print(even)


word = input()
valid = False
# both 'a' and 'z' are in lower case
if 'a' <= word[0] <= 'z':
    if word[0] == word[-1]:
        valid = True
print(valid)


num = input()
first, middle, last = int(num[0]), int(num[1]), int(num[2])
if first + last == middle:
    print('sandwich')
else:
    print('plain')
"""

x = int(input())
y = int(input())
z = int(input())


# Block-1 Start
if x > 0 or y > 0 or z > 0:
    if (x > 0 and y > 0) or (y > 0 and z > 0) or (z > 0 and x > 0):
        if x > 0 and y > 0 and z > 0:
            print('P3')
        else:
            print('P2')
    else:
        print('P1')
# Block-1 End

# Block-2 Start
if x < 0 or y < 0 or z < 0:
    if (x < 0 and y < 0) or (y < 0 and z < 0) or (z < 0 and x < 0):
        if x < 0 and y < 0 and z < 0:
            print('N3')
        else:
            print('N2')
    else:
        print('N1')
# Block-2 End

