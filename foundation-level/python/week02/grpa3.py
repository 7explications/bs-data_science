# CODE WITH ALGORITHM
# Step-1: accept the text as input into a variable called string
# Step-2: convert string to lower case; reassign the lower case version of text to string itself
# Step-3: define a variable called vowels; initialise it to the empty string
# Step-4: check if 'a' is in the variable string; if it is, concatenate 'a' to vowels at the end
# Step-5: check if 'e' is in the variable string; if it is, concatenate 'e' to vowels at the end
# Step-6: check if 'i' is in the variable string; if it is, concatenate 'i' to vowels at the end
# Step-7: check if 'o' is in the variable string; if it is, concatenate 'o' to vowels at the end
# Step-8: check if 'u' is in the variable string; if it is, concatenate 'u' to vowels at the end
# Step-9: if vowels is empty, print 'none'
# Step-10: if vowels is not empty, print vowels

string= input()
string=string.lower()
vowels=""
if "a" in string:
    vowels+="a"
if "e" in string:
    vowels+="e"
if "i" in string:
    vowels+="i"
if "o" in string:
    vowels+="o"
if "u" in string:
    vowels+="u"    
if  vowels=="":
    print ("none")
else:
    print(vowels)    

