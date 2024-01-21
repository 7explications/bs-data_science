"""
Accept the date in DD-MM-YYYY format as input and print the year as output.
"""
import os
os.system("cls")
dt=input()
ar=dt.split("-")
print(ar[2])