#Accept a positive integer n as input, where n>1. Print PRIME if n is a prime number and NOTPRIME otherwise.
num=abs(int(input()))
i=2
prime=True
while(i<num):
    if num%i==0:
        prime=False
    i+=1
if prime==True and num>=2:
    print("PRIME")
else:
    print("NOTPRIME")
        


