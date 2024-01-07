import os #importing os library
import re #importing  regular expressions.
os.system('cls') # this line execte cls os command, anc will clear scree.

#Strings and user input
#Single and double quoted strings
print("-"*50,"\n") # "-"*50 will print - char 50 times 
#The most common way to declare string literals is by enclosing a sequence of characters within single or double quotes. Unlike other scripting languages like Bash, Perl and Ruby, there is no feature difference between these forms. Idiomatically, single quotes are preferred and other variations are used when needed.
#REPL will again be used predominantly in this chapter. One important detail to note is that the result of an expression is displayed using the syntax of that particular data type. Use print() function when you want to see how a string literal looks visually.
print ('This is single quoted string')
print ("This is double quoted string")
single = 'single quoted string stored in vaiable'
double = 'double quoted string stored in vaiable'
print (single)
print (double)

print("-"*50,"\n")
#If the string literal itself contains single or double quote characters, the other form can be used.
print('"Will you come?" he asked.')

print("-"*50,"\n")
#Use the \ character to escape the quote characters, , \' and \" will evaluate to ' and " characters respectively.
print('"It\'s so pretty!" can I get one?')
print("\"It's so pretty!\" can I get one?")

print("-"*50,"\n")
#\n epresents the newline character, \t is for tab character
print('hi there.\nhow are you?')
print('hi there.\thow are you?')

print("-"*50,"\n")
#can also declare multiline strings by enclosing the value with three single/double quote characters
print('''this this 
multyline 
    sente.
and print as you write''')

student = '''\
Name:\tlearnbyexample
Age:\t25
Dept:\tCSE'''

print(student)

print("-"*50,"\n")
#Raw strings, in python r'' or r"", use for raw string
print(r'item\tquantity')
print(r"item\nquantity\'")

print("-"*50,"\n")
#also we can use re built-in module for regular expressions. for this have to import  re module 
#numbers >= 100 with optional leading zeros
numbers=re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')
print(numbers)

print("-"*50,"\n")
#String operators
#to concatenate strings using the + operator. 
str1 = 'first word'
str2 = 'second word'
str3 = str1 + str2
print(str3)

# can repeat a string by using the * operator between a string and an integer.
style_char = '.'
print(style_char * 10)

style_char = '#'
print(style_char * 5)

#String formatting
name = 'Jitendra'
age = 48
str=f'Name: {name}, Age:{age}'
print(str)
print("Name: {}, Age:{}".format(name,age))

num1 = 42
num2 = 7
print("total of {:3d} and {:3d} is {:3d}".format(num1,num2, num1+num2))

appx_pi = 22 / 7
print("Approx pi:{:.5f}".format(appx_pi))

# alignment Left
fruit = 'apple'
print("{:<20}".format(fruit))
print("{:-<20}".format(fruit))

# alignment Right
print("{:>20}".format(fruit))
print("{:->20}".format(fruit))
# alignment Center
print("{:^20}".format(fruit))
print("{:-^20}".format(fruit))

#can use b, o and x to display integer values in binary, octal and hexadecimal formats
num = 98
print("binary of {} is {:b}".format(num,num))
print("octal of {} is {:o}".format(num,num))
print("hexadecimal of {} is {:x}".format(num,num))
num1=50
num2=70
total= 'Total is:[%5d]' % (num1+num2)
print(total)

