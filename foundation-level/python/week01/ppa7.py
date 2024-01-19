"""
Accept a five digit number as input and print the sum of its digits as output.
"""
import os
os.system("cls")
n=int(input())
s=str(n)
i=0
len=len(s)
sum=0
while i<len:
    sum+=int(s[i])
    i+=1
print(sum) 