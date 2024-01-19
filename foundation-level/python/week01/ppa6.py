"""
Accept the registration number of a vehicle as input and print its state-code as output.
"""
import os
os.system("cls")
rno=input()
arr=rno.split("-")
print(arr[0])