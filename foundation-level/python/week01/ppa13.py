"""
The following expression is called a continued fraction:

x+  1
   -------- 
    x +     1
        -------------------
        x+      1
            ----------------
            x +   1
                -----------------
                x+    1
                    -----
                      x
Accept a positive integer x as input, compute the value of this continued fraction and store the result in a variable named cfrac. We will round off your answer to exactly two decimal places. You don't have to print the output to the console, we will take care of that.


"""

import os
os.system("cls")

x=int(input())
cfrac = x+(1/(x+(1/(x+(1/(x + (1/ (x + (1/x)))))))))

print(cfrac)