"""
Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
"""
import os
os.system("cls")
sn=input()
na=sn.split(",")
sum=1
for i in na:
    sum*=int(i)
print(sum)    