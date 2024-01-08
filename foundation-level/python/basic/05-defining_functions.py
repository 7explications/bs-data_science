import os #importing os library
#Defining functions
#how to define your own functions, pass arguments to them and get back results.
#def : Use the def keyword to define a function. The function name is specified after the keyword, followed by arguments inside parentheses and finally a : character to end the definition.
#Arguments are optional
def clearScreen(): #clear screen
    os.system('cls')

def dir(): #show current dir list
    os.system('dir')    

def greeting():
    print('-----------------------------')
    print('Hello python function        ')
    print('-----------------------------')   

#Accepting arguments
#Functions can accept one or more arguments, specified as comma separated variable names
def greetingMessage(msg):
    op_length = 10 + len(msg)
    styled_line = '-' * op_length
    print(styled_line)
    print(f'{msg:^{op_length}}')
    print(styled_line)      

#Default valued arguments
def greetingLeftMessage(msg, style='-', spacing=10):
    op_length = spacing + len(msg)
    styled_line = style * op_length
    print(styled_line)
    print(f'{msg:<{op_length}}')
    print(styled_line)     


def greetingRightMessage(msg, style='-', spacing=10):
    op_length = spacing + len(msg)
    styled_line = style * op_length
    print(styled_line)
    print(f'{msg:>{op_length}}')
    print(styled_line)       

def greetingCenterMessage(msg, style='-', spacing=10):
    op_length = spacing + len(msg)
    styled_line = style * op_length
    print(styled_line)
    print(f'{msg:^{op_length}}')
    print(styled_line) 

#Return value
#The default return value of a function is None, which is typically used to indicate the absence of a meaningful value.
def num_add(num1, num2):
    return num1+num2    

def num_sub(num1, num2):
    return num1-num2 

def num_mul(num1, num2):
    return num1*num2 

def num_div(num1, num2):
    return num1/num2 

def num_div_int(num1, num2):
    return num1//num2

def num_sqr(num1, num2):
    return num1**num2  

def num_mod(num1, num2):
    return num1%num2  


clearScreen()
n1=11
n2=2
f1=23.5
f2=3.3
greeting()
greetingMessage("Jitebdra")
greetingLeftMessage("Jitebdra")
greetingLeftMessage("Jitebdra","#")
greetingLeftMessage("Jitebdra", "-", 20)
greetingRightMessage("Jitebdra", "-", 20)
greetingCenterMessage("Jitebdra", "-", 20)

# + for addition
print("{} + {} = {}".format(n1,n2, num_add(n1,n2)) )
print("{} + {} = {}".format(f1,f2, num_add(f1,f2)) )

# - for subtraction
print("{} - {} = {}".format(n1,n2, num_sub(n1,n2)) )
print("{} - {} = {}".format(f1,f2, num_sub(f1,f2)) )

# * for multiplication
print("{} * {} = {}".format(n1,n2, num_mul(n1,n2)) )
print("{} * {} = {}".format(f1,f2, num_mul(f1,f2)) )

# ** for exponentiation
print("{} ** {} = {}".format(n1,n2, num_sqr(n1,n2)) )
print("{} ** {} = {}".format(f1,f2, num_sqr(f1,f2)) )


#division
#two operators for division. Use / if you want a floating-point result. Using // between two integers will give only the integer portion of the result (no rounding).
# / if you want a floating-point result
print("{} / {} = {}".format(n1,n2, num_div(n1,n2)) )
print("{} / {} = {}".format(f1,f2, num_div(f1,f2)) )

# // between two integers will give only the integer portion of the result (no rounding)
print("{} // {} = {}".format(n1,n2,  num_div_int(n1,n2)) )
print("{} // {} = {}".format(f1,f2,  num_div_int(f1,f2)) )

#remainder
#modulo operator % to get the remainder
print("{} % {} = {}".format(n1,n2, num_mod(n1,n2)) )
print("{} % {} = {}".format(f1,f2, num_mod(f1,f2)) )


