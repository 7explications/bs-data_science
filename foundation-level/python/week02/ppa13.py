a_f_s=int(input())
a_f_w=int(input())
a_s_s=int(input())
a_s_w=int(input())

b_f_s=int(input())
b_f_w=int(input())
b_s_s=int(input())
b_s_w=int(input())

a_total=a_f_s+a_s_s
b_total=b_f_s+b_s_s

if (a_total>b_total and b_s_w==10):
    print("Team A")
elif (b_total>a_total):
    print("Team B")
else:
    print("DRAW")
