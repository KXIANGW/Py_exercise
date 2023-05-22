'''
# Exercise 1
# 1. 定義一個 square 的函數，參數為 num，並回傳 num 的平方數
def square(num):
    return num*num
# 2. 定義一個 add 的函數，參數為 num1, num2，並回傳兩數之和
def add(num1,num2):
    return num1+num2
# 3. 定義一個 sqrt 的函數，參數為 num，並回傳 num 的平方根
def sqrt(num):
    return num**0.5
# 4. 透過以上三個函式計算出直角三角形之斜邊c(三邊為a, b, c)
a = int(input('Input a: '))
b = int(input('Input b: '))
c = sqrt(add(square(a),square(b)))
print('c:',c)
'''

'''
# Exercise 2
# 1. 定義一個函式 isPrime 判斷其數字是否為質數
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
# 2. 透過 isPrime 將1~100的質數全部輸出出來
for i in range(1,101):
    if isPrime(i):
        print(i,end=' ')
print()
'''

'''
# Exercise 3
# 解多項式
# 設計一個函式可以回傳每一個多項式各項的數值(ex: 2x^2,x = 1 -> item = 2)
def item(coef,expon,x):
    return coef*(x**expon)

coef = [2,1,-4,5]
expon = [4,3,1,0]
x = float(input('X: '))
y = 0

for i in range(len(coef)):
    y += item(coef[i],expon[i],x)
print('Y:',y)
'''

'''
# Exercise 4
# 1. 定義 rec_area 一個函式，參數為x,y，並回傳矩形的面積
def rec_area(x,y):
    return x*y

# 2. 定義一個 rec_perimeter 函式，參數為x,y，並回傳矩形的周長
def rec_perimeter(x,y):
    return 2*(x+y)

# 3. 自訂一個存放矩形邊長的 list ，並透過定義好的函式來輸出其面積、周長
recs = [[5,6],[int(input('x: ')),int(input('y: '))]]
i = 1
for data in recs:
    print('Rec'+str(i))
    print('area:',rec_area(data[0],data[1]))
    print('perimeter:',rec_perimeter(data[0],data[1]))
    i+=1
'''

# Exercise 5
# 定義一個 isPalindromes 函式判斷一段文字是否為回文，並回傳其結果
def isPalindromes(text):
    for i in range(len(text)//2):
        if text[i]!=text[len(text)-i-1]:
            return False
    return True

wordList = ['puppy','level','college','wow']
for word in wordList:
    if isPalindromes(word):
        print(word,'is palindromes')
    else:
        print(word,'is not palindromes')