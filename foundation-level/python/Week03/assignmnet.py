"""

n = int(input())
for i in range(1, 11):
    print(n * i)

    


n = int(input())
i = 1
while (i <= n):
    if (n % i == 0):
        print(i)
    i = i + 1



for num in range(1, 11):
    if num % 2 == 0:
        print(num)



x=0
while True:
    x+=1
    if ((x**2)+x+41)%41==0:
        break
print(x)    
        




t=0
i = 0
while (i < 100):
    print(i * '*')
    t=t+i
    i = i + 1

print(t)   



for char in 'a1b2c3d4e5':    
    if char in 'abcde':
        print('|', end = '') # there is no space between the quotes
        continue    
    print(char, end = '')  # there is no space between the quotes
print('|')


x = int(input())
y = 0
while x > 1:
    x = x // 2
    y = y + 1
print(y)


x = int(input())
i = 0
while x % (10 ** i) != x:
    i = i + 1
print(i)


alpha = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
word = 'python'
encoded_word = ''  # there is no space between quotes
for char in word:
    shifted_index = (alpha.index(char) + shift) % 26
    encoded_char = alpha[shifted_index]
    encoded_word += encoded_char
print(encoded_word)
 

name = input()
nick = ''    # there is no space between the quotes
space = ' ' # there is one space between the quotes
first_char = True
for char in name:
    if first_char == True:
        nick = nick + char
        first_char = False
    if char == space:
        first_char = True
print(nick)


word = input()
valid = True
for i in range(len(word)):
    char = word[i]
    if i % 2 == 0 and char not in 'aeiou':
        valid = False
print(valid)


n = int(input())
F_prev = 1
F_curr = 1
count = 2
while count < n:
    temp = F_prev + F_curr
    F_prev = F_curr
    F_curr = temp
    count += 1
print(F_curr)


n = int(input())
if n <= 2:
    print(1)
else:
    F_prev = 1
    F_curr = 1
    count = 2
    while count < n:
        temp = F_prev + F_curr
        F_prev = F_curr
        F_curr = temp
        count += 1
    print(F_curr)


l=0
for x in range(100):
    for y in range(100):
        if x != y:
            print(f'{x},{y}')
            l=l+1
print(l)          



x, y = 0, 0
while x < 100:
    y = 0
    while y < 100:
        if x != y:
            print(f'{x},{y}')
        y += 1
    x += 1


"""

x, y = 0, 0
while x < 100:
    while y < 100:
        if x != y:
            print(f'{x},{y}')
    y += 1
    x += 1