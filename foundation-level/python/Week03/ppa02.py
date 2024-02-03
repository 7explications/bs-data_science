#Accept a positive integer n as input and print all the factors of n, one number on each line.

num=abs(int(input()))
i=1
while(i<=num):
    if num%i==0:
        print(i)
    i+=1