"""
You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a substring in the given string. 
Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.
The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.
"""
import os
os.system("cls")

word=input()
start=int(input())
end=int(input())
sub=word[start:end+1]
i=0
new_str=""
while i<=len(word):
    new_str+=sub
    i=len(new_str)
print(new_str)  