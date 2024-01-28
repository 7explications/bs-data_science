"""
Print positive if it is greater than zero and negative if it is less than zero. You can assume that the input will be non-zero.
"""
import os
os.system("cls")

number=int(input("Enter Non Zero number: "))
if number>0:
    print("positive")
elif number <0:
    print("negative")
else:
    print("You entered 0")
