"""
Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end.
"""
import os
os.system("cls")

i=0
str=""
while i<5:
    str+= input() 
    i+=1
    if i<5:
        str+=" "
    else:
        str+="."
print(str)