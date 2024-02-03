# Two integers are co-prime if the only common divisor between the two integers is one.
# Accept two positive integers as input in two different lines. Print Coprime if the two integers are co-prime, else print Not Coprime. 
# Assume that both the integers are greater than two.

a=int(input())
b=int(input())
if a<b:
    smlr=a
else:
    smlr=b
coprime=True     
for i in range(2,smlr+1):
    if a%i==0 and b%i==0:
        coprime=False
if coprime==True:
    print("Coprime")
else:
    print("Not Coprime")
    

