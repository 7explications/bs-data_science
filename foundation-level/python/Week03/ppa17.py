"""
Consider two non-empty strings a and b of lengths n1 and n2 respectively, which contain only numbers as their characters. 
Both the strings are in ascending order, that is a[i]≤a[j] for 0≤i<j<n1. 
The same holds true for b. You need to merge both the strings into one string of length n1+n2 such that all the characters of this combined string are also in ascending order.
Accept a and b as input and print this merged string as output.
"""
a=input()
b=input()
word=list(a+b)
l=len(word)
for i in range(l):
    for j in range(i+1, l):
        if int(word[i])>int(word[j]):
            word[i], word[j] = word[j], word[i]
asnd_word=''.join(word)
print(asnd_word)
         