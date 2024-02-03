num=abs(int(input()))
sum=0
for i in range(1,num+1):
    for j in range(1,i+1):
        sum=sum+j
print(sum)           