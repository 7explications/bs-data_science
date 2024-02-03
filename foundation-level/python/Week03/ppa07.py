# Accept a positive integer as input and print the sum of the digits in the number.
num=abs(int(input()))
str_num=str(num)
sum=0
for i in str_num:
    sum+=int(i)
print(sum)    
    