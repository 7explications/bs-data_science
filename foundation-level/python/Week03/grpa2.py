num= abs(int(input()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

fact=[]
for i in range(1,num+1):
    for j in range(i+1,num+1):
        if i*j==num:
            if i>1 and i<num:
                fact.append(i)
            fact.append(j)  

for f in fact:
    if is_prime(f)==True:
        print(f)            