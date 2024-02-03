# Accept a positive integer n as input and find all solutions to the equation:
# x^2 + y^2 = z^2 
# subject to the following constraints:
# (a) x, y and  z are positive integers 
# (b) x<y<z<n

num=abs(int(input()))
sulution=False
for x in range(1,num+1):
    for y in range(x+1,num+1):
       for z in range(y+1, num+1):
        x2=x**2
        y2=y**2
        z2=z**2
        if ((x2 + y2) == z2) and z<num:
           print(f"{x},{y},{z}")
           sulution=True
if sulution==False:
    print("NO SOLUTION")