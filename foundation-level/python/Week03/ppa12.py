#Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. 
# Print this new string as output. You can assume that all input strings will be in lower case.

str1=input()
str2=input()
str1=str1.lower()
str2=str2.lower()
word=""
for i in str2:
    if i not in str1:
      word+=i
print(word)      
            