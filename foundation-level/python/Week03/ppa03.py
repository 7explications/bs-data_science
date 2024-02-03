# Accept two positive integers a and b as input. 
# Print the sum of all integers in the range [1000, 2000], endpoints inclusive, that are divisible by both a and b. 
# If you find no number satisfying this condition in the given range, then print 0.

a=abs(int(input()))
b=abs(int(input()))
sum=0
for num  in range(1000,2001):
    if num%a==0 and num%b==0:
        sum+=num

if sum!=0:
    print(sum)
else:
    print(0)