# Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. 
# You can assume that the string will only contain letters.
word=input()
word=word.lower()
word_list=list(word)
l=len(word_list)
for i in range(0,l):
    for j in range(i+1,l):
        if word_list[i]>word_list[j]:
            word_list[i], word_list[j]=word_list[j], word_list[i]
print("".join(word_list))