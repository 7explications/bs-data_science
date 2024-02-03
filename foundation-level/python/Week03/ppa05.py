#Accept a sequence of positive integers as input and print the the maximum number in the sequence. The input will have n+1 lines, where n denotes the number of terms in the sequence. 
# The i-th line in the input will contain the i-th term in the sequence for 1≤i≤n. The last line of the input will always be the number 0. 
# Each test case will have at least one term in the sequence.

max=0
while True:
    num=abs(int(input()))
    if num==0:
        break
    if num>max:
        max=num
print(max) 


