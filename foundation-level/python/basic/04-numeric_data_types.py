import os #importing os library
os.system('cls')
#Numeric data types
#int : Integer numbers are made up of digits 0 to 9 and can be prefixed with unary operators like + or -. There is no restriction to the size of numbers that can be used, only limited by the memory available on your system
a=40
print(a)
b=10_000_00
print(b)
print(a+10)
print(b-29)

# floating-point numbers
f=3.14
print(f)
f=f-1
print(f)

#Arithmetic operators
n1=11
n2=2
f1=23.5
f2=3.3
#All arithmetic operators you'd typically expect are available, If any operand is a floating-point number, result will be of float data type. Use + for addition, - for subtraction, * for multiplication and ** for exponentiation.
# + for addition
print("{} + {} = {}".format(n1,n2,(n1+n2)) )
print("{} + {} = {}".format(f1,f2,(f1+f2)) )

# - for subtraction
print("{} - {} = {}".format(n1,n2,(n1-n2)) )
print("{} - {} = {}".format(f1,f2,(f1-f2)) )

# * for multiplication
print("{} * {} = {}".format(n1,n2,(n1*n2)) )
print("{} * {} = {}".format(f1,f2,(f1*f2)) )

# ** for exponentiation
print("{} ** {} = {}".format(n1,n2,(n1**n2)) )
print("{} ** {} = {}".format(f1,f2,(f1**f2)) )


#division
#two operators for division. Use / if you want a floating-point result. Using // between two integers will give only the integer portion of the result (no rounding).
# / if you want a floating-point result
print("{} / {} = {}".format(n1,n2,(n1/n2)) )
print("{} / {} = {}".format(f1,f2,(f1/f2)) )

# // between two integers will give only the integer portion of the result (no rounding)
print("{} // {} = {}".format(n1,n2,(n1//n2)) )
print("{} // {} = {}".format(f1,f2,(f1//f2)) )

#remainder
#modulo operator % to get the remainder
print("{} % {} = {}".format(n1,n2,(n1%n2)) )
print("{} % {} = {}".format(f1,f2,(f1%f2)) )

