# Accept a positive integer n as input and print a "number arrow" of size n. 
# For example, n=5 should produce the following output:
"""
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
"""

num= abs(int(input()))
wls=[]
for i in range(1,num+1):
    ls=[]
    for j in range(1,i+1):
        ls.append(str(j))
        if j<i:
            ls.append(",")
    print("".join(ls)) 
for i in range(num,1,-1):
    ls=[]
    for j in range(1,i):
        ls.append(str(j))
        if j<i-1:
            ls.append(",")
    print("".join(ls))  
    
   
    