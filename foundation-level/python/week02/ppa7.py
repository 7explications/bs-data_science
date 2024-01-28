"""
A sequence of five words is called magical if the i th, word is a substring of the (i=1) word for every i in the range 1<=i<5. 
Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and non-magical otherwise.
Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.

"""
import os
os.system("cls")

str_1=input()
str_2=input()
str_3=input()
str_4=input()
str_5=input()
d=[str_2, str_3, str_4, str_5]
magical=True
for i in d:
    if str_1 not in i:
        magical=False

if magical:
    print("magical")    
else:
   print("non-magical")  