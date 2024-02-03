# Accept a positive integer n as input and print a triangle of zeros for n lines. 
# The i-th line should have i zeros. There shouldn't be any spaces between consecutive zeros. 
# Do not print a space at the end of a line.

num=abs(int(input()))
for i in range(1,num+1):
    print("0"*i)