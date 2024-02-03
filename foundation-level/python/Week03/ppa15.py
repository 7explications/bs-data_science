num=input()

isFloat=False
isDigit=False

try:
    float_value = float(num)
    isFloat=True
except ValueError:
    isFloat=False

if num.isdigit()==True:
    isDigit=True

if float_value==True:
    print("Float")
elif  isDigit==True:
    print("Integer")
else:
    print("None")           