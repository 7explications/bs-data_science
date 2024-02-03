# Accept a positive integer n as input and print the sum of all prime numbers in the range [1,n], endpoints inclusive. 
# If there are no prime numbers in the given range, then print 0.

num=abs(int(input()))
sum=0
for i in range(1,num+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime==True and i>=2:
        sum+=i
print(sum) 