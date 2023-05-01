# Exercise 1
'''
begin = int(input('begin: '))
end = int(input('end: '))
sum = 0
d = 1
while begin<=end:
    print(begin)
    sum+=begin
    begin+=d
print('Sum:', sum)
'''

# Exercise 2
'''
num1 = int(input('num1: '))
num2 = int(input('num2: '))
sum = 0
if num1%2==0:
    num1+=1
while num1<=num2:
    print(num1)
    sum+=num1
    num1+=2
print('Sum:',sum)
'''

# Exercise 3
'''
length = float(input('length: '))
width = float(input('width: '))
while length <=0 or width<=0:
    print('Cannot form rectangle!\nPls try again')
    length = float(input('length: '))
    width = float(input('width: '))
# 1. 輸出長方形周長
print('permiter:',(length+width)*2)
# 2. 輸出長方形的面積
print('area:', length*width)
'''


# Exercise 4
# 請使用者輸入一個數字，並嘗試輸入欲減或欲加的數，使原本的數字變為0，並記錄運用了多少加法、減法
'''
num = int(input('num: '))
add_count = 0
minus_count = 0
while num !=0:
    num2 = int(input('num2: '))
    if num > 0:
        num-=num2
        minus_count +=1
    else:
        num+=num2
        add_count +=1
    if num > 0:
        print('num is positive')
    elif num < 0:
        print('num is negative')
    else:
        print('num is zero')
print('\nThe End!')
print('+:',add_count)
print('-:',minus_count)
'''

# Exercise 5
# 自訂一個多項式
# 1. coef = [], expon = []
# 2. 使用者依照個人興趣設計多項式
# 3. 輸入 x 獲得其解 f(x)

coef = []
expon = []
while True:
    term = input('Term(-1表示結束): ').split('x^')
    if term == ['-1']:
        break
    coef+=[int(term[0])]
    expon+=[int(term[1])]
print('coef:',coef)
print('expon:',expon)
x = float(input('x: '))
y = 0
for i in range(len(coef)):
    y+=coef[i]*(x**expon[i])
print('f(x):',y)

