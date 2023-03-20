'''
#Exercise 1
num = int(input("Pls input integer: "))
if num>=0:
    print(num)
else:
    print(-num)
'''


'''
#Exercise 2
a = int(input("a: "))
b = int(input("b: "))
if(a>b): 
    a,b=b,a
print(b-a)
'''


'''
#Exercise 3
score = int(input("Score: "))
grade = ""
if(score>=90):
    grade = 'A'
elif(score>=80):
    grade = 'B'
elif(score>=70):
    grade = 'C'
elif(score>=60):
    grade = 'D'
else:
    grade = 'F'
print("Your grade is:",grade)
'''



#Exercise 4
# 判斷 num1 是否為 num2 的倍數
# 請輸入目標數 num1 (0<num1<=100) 再輸入 num2 (0<num2<=num1)
num1 = int(input("num1: "))

if(0<num1 and num1<=100):
    num2 = int(input("num2: "))
    if(0<num2 and num2<=num1):
        if(num1%num2==0):
            print(True)
        else:
            print(False)
    else:
        print("num2 範圍錯誤")
else:
    print("num1 範圍錯誤")


'''
#Exercise 5
# 請先定義 box = ['apple', 'waterlemon', 'wax apple', 'lemon', 'pineapple']
# ，而使用者選擇 1、2來選擇要拿走或者放入水果，而其水果是使用者手動輸入的
# 1. 試著刪除 apple 和放入 strawberry
# 2. 試著刪除 banana 和 放入 lemon 
# 3. 試著選擇 1、2 以外的數字
box = ['apple', 'waterlemon', 'wax apple', 'lemon', 'pineapple']
choise = input("請選擇模式(1)從 box 中拿走水果 (2) 放入水果: ")

if choise == '1':
    fruit = input("挑選水果: ")
    if fruit in box:
        box.remove(fruit)
        print(box)
    else:
        print(fruit+"不在 box 中")
    
elif choise == '2':
    fruit = input("挑選水果: ")
    if fruit not in box:
        box.append(fruit)
        print(box)
    else:
        print(fruit+"已經存在 box 中")
    
else:
    print("無此功能")
'''