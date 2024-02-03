#Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.

word=input()
rev_word=""
for i in word:
    rev_word = i+rev_word
if  word==rev_word:
    print("PALINDROME")    
else:
    print("NOT PALINDROME")
    