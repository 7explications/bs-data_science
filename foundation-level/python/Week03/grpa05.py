# Accept a phone number as input. A valid phone number should satisfy the following constraints.
# (1) The number should start with one of these digits: 6, 7, 8, 9
# (2) The number should be exactly 10 digits long.
# (3) No digit should appear more than 7 times in the number.
# (4) No digit should appear more than 5 times in a row in the number.
# If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.
# Print the string valid if the phone number is valid. If not, print the string invalid.

num= str(abs(int(input())))
is_valid=True
num_list=list(num)
l= len(num_list)
start_digits=["6","7","8","9"]
if num_list[0] not in start_digits:
    is_valid=False
if l!=10:
    is_valid=False
for i in num_list:
    if num_list.count(i)>7:
        is_valid=False
count=1
for m in range(1,l):
    if num_list[m] == num_list[m - 1]:
        count += 1
        if count > 5:
            is_valid=False
    else:
        count=1        

if is_valid==True:
    print("valid")
else:
    print("invalid")


