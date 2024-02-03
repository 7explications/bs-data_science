# Accept a sequence of words as input and print the the shortest word in the sequence. 
# The input will have n+1 lines, where n denotes the number of terms in the sequence. 
# The i-th line in the input will contain the i-th word in the sequence for 1≤i≤n.
# The last line of the input will always be the string abcdefghijklmnopqrstuvwxyz. 
# This string is not a part of the sequence. You can assume that each test case corresponds to a non-empty sequence of words. 
# If there are multiple words that have the same minimum length, print the first such


ln=65536
min_word=""
end_word="abcdefghijklmnopqrstuvwxyz"
while True:
    word=input()
    if word==end_word:
        break
    if len(word)<ln:
        min_word=word
        ln=len(word)
print(min_word)        
        