# MISSING CODE
e1 = int(input())
e2 = int(input())
e3 = int(input())
e4 = int(input())
e5 = int(input())

if (e1<1 or e2<1 or e3<1 or e4<1 or e5<1):
    print('NO')
elif (e1+ e2) % 2 != 0:
    print('NO')    
elif (e2+ e3) % 2 != 0:
    print('NO')
elif (e3+ e4) % 2 != 0:
    print('NO')
elif (e4 + e5) % 2 != 0:
    print('NO')
elif (e5 + e1) % 2 != 0:
    print('NO')
else:
    print('YES')