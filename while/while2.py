'''
# Exercise 1
# 1. 請輸入一個數字，並輸出其為偶數或奇數
num = int(input('Pls input num: '))
if num%2==0:
    print('Num is even')
else:
    print('Num is odd')

# 2. 請依序輸入五個數字，並輸出其為偶數或奇數 (for、while)
# for
for i in range(5):
    num  = int(input('Pls input num: '))
    if num%2==0:
        print('Num is even')
    else:
        print('Num is odd')

# while
n = 5
while n!=0:
    num  = int(input('Pls input num: '))
    if num%2==0:
        print('Num is even')
    else:
        print('Num is odd')
    n-=1


# 3. 請依序輸入數字，並輸出其為偶數或奇數(輸入break -> 結束)
num = input('Pls input num: ')
while num != 'break':
    num = int(num)
    if num%2==0:
        print('Num is even')
    else:
        print('Num is odd')
    num = input('Pls input num: ')
print('End')
'''


# Eeercise 2
# 1. 透過 for loop 計算1~100的和
sum = 0
for i in range(1,101):
    sum+=i
print('Sum:',sum)
# 2. 透過 while loop 計算1~100的和
sum = 0
n = 1
while n<101:
    sum+=n
    n+=1
print('Sum:',sum)
# 3. 透過 while loop 計算1~100且公差(d)為2的和
sum = 0
n = 1
d = 2
while n<101:
    sum+=n
    n+=d
print('Sum:',sum)

# Exercise 3
# 1. 透過 while loop 印出 1~16的數
n  = 1
while n <=16:
    print(n)
    n+=1
    
# 2. 透過 while loop 印出 1~16的數且公差(d)為2
n = 1
while n<=16:
    print(n)
    n+=2