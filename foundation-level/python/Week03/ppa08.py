# Accept a positive integer n as input and print the first n integers on a line separated by a comma.


num=abs(int(input()))
w=""
for i in range(1,num+1):
    w+=str(i)+","
w=w[:len(w)-1]    
print(w)
