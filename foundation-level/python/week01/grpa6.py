"""
Accept two positive integers M and N as input. There are two cases to consider:

(1) If M < N, then print M as output.

(2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N, then subtract N from M1 and call the difference M2. 
    Keep doing this operation until you reach a value k, such that, Mk < N. You have to print the value of Mk as output. 
    You should be able to solve this problem using the concepts covered in week-1.
"""

import os
os.system("cls")

def num(m,n):
    if(m<n):
        return m
    else:
        m1=m
        while m1>=n:
            m1-=n
        return m1    
      

m=int(input())
n=int(input())
s=num(m,n)
print(s)