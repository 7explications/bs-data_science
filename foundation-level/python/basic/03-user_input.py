import os #importing os library
import re #importing  regular expressions.
os.system('cls') # this line execte cls os command, anc will clear scree.

#User input
#The input() built-in function can be used to get data from the user. It also allows an optional string to make it an interactive process.
name = input('what is your Name?:') #string input
age = int(input('what is your Age?:')) #int input
print("your name is:", name)
print("and age is:", age)

#Type conversion
#The type() built-in function can be used to know what data type you are dealing with. You can pass any expression as an argument
print("tyoe of {} is {}".format(name, type(name)))
print("tyoe of {} is {}".format(age, type(age)))
print("tyoe of {}/3 is {}".format(age, type(age/3)))

