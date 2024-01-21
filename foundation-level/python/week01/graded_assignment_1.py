"""
Graded Assignment 1
"""
import os
os.system("cls")

"""
Q1. What is the type of the following expression?
1 + 4 / 2
"""

print("Q1. type of 1 + 4 / 2 is ", type(1 + 4 / 2))

"""
Q2. What is the type of the following expression?
(1 > 0) and (-1 < 0) and (1 == 1)
"""
print("Q2. (1 > 0) and (-1 < 0) and (1 == 1) ", type((1 > 0) and (-1 < 0) and (1 == 1)))

"""
Q3. Convert the following mathematical statement into a Python expression.
10^3 +9^3 = 12^3 +1^3 =1729
"""
result = (10**3 + 9**3) == (12**3 + 1**3) == 1729
print("Q3. (10**3 + 9**3) == (12**3 + 1**3) == 1729",result)

"""
Q4. E_1 and E_2 are Boolean values. Consider the following expression.
E_3 = not (E_1 or E_2)
E_4 = (not E_1) and (not E_2)
print(E_3 == E_4)
What can you say about the value printed by the code given above?
1. It is True if and only if both E_1 and E_2 have the same value.
2. It is False if and only if both E_1 and E_2 have the same value.
3. It is always True.
4. It is always False.
"""
E_1 = False
E_2 = True
E_3 = not (E_1 or E_2)
E_4 = (not E_1) and (not E_2)
print("Q4. It is always True" ,E_3 == E_4)

"""
Q5. E is a boolean variable. Consider the following sequence of expressions:
not E
not not E
not not not E
not not not not E
.
.
.
This pattern keeps repeating for a thousand lines. If line number 500 evaluates to False, what is the value of E?
a. True
b. False
c. Cannot be determined

"""
print("Q5.","So, if line 500 evaluates to False, it implies that the original boolean variable E must be True.")

"""
Consider the following string:
word = '138412345678901938'
For what values of a and b does the following expression evaluate to True? Assume that both a and b are positive integers.
word[a : b] == '123456789'
"""
word = '138412345678901938'
a=4
b=13
s = word[a : b]

"""
Q6 Enter the value of a.
"""
print("Q6.", "Vlaue of a is ", a)


"""
Q7 Enter the value of b.
"""
print("Q7.", "Vlaue of b is ", b)

"""
Q8. We need to write a program that performs this task: accept two names (strings) as input. 
Print True if the first name comes before the second in alphabetical order, and False otherwise. Sample test cases:
Input               Output
sachin      rohit   False
saina       sindhu  True

For example, sachin comes after rohit, so the expected output is False. 
Assume that all names consist of just one word and will be entered in lower case during the time of input. 
Select all correct implementations of this program.

"""
print ("""
Q8. 
    name1 = input()
    name2 = input()
    print(name1 < name2)
       
    print(input() < input())

    name1 = input()
    name2 = input()
    result = name1 < name2
    print(result)       
       
       
""")

"""
Q9. What is the output of the following snippet of code?
"""
x = 2 ** 5
x1 = x // 2
x2 = x1 // 2
x3 = x2 // 2
x4 = x3 // 2
x5 = x4 // 2
print("Q9.",x1 + x2 + x3 + x4 + x5)


