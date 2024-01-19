
"""
Print the following pattern. There is exactly one space between any two consecutive numbers on any line. There are no spaces at the end of any line.
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""
import os
os.system("cls")
rows=5
for i in range(2, rows + 1):
    line=""
    for j in range(1, i + 1):
        line+=str(j)+" "
    for j in range(i - 1, 0, -1):
        line+=str(j)+" "
    line=line[0:len(line)-1]    
    print(line)