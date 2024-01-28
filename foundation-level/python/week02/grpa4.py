"""
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. 
If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order 
(names will follow Python's capitalize case format).
The input will have four lines. The first two lines correspond to the first person, 
while the last two lines correspond to the second person. 
For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. 
Your output should be the name of the younger of the two.
"""
from datetime import *
name1=input()
age1=input()
dt1=datetime.strptime(age1,"%d-%m-%Y").date()
name2=input()
age2=input()
dt2=datetime.strptime(age2,"%d-%m-%Y").date()

if (dt1==dt2):
    if(name1.upper()<name2.upper()):
        print(name1)
    else:
        print(name2)
elif (dt1>dt2): 
    print(name1)
else:   
    print(name2)
