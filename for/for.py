#Exercise 1
# begin = int(input('Begin: '))
# end = int(input('End: '))
# sum = 0
# for num in range(begin,end+1):
#     sum+=num
#     print(num)
# print('Sum:',sum)

#Exersice 2
# mydata = []
# num = int(input('num: '))
# for i in range(num):
#     mydata+=[input(str(i+1)+'. Input mydata: ')]
# for i in mydata:
#     print(i)

# Exercise #3
# n = int(input('n: '))
# for star_num in range(1,n+1):
#     print(star_num*'*')

# Exercise #4
# 請先定義一個 num_list = [2,8,1,4,5,11,3,7,10,9]
# num_list = [2,8,1,4,5,11,3,7,10,9]

# # 1. 請使用者輸入一個整數 num，並透過此整數將 num_list 進行分割，將其分割成大於、小於、等於 num 的list(bigger、smaller、equal)
# bigger = []
# smaller = []
# equal = []
# num = int(input('num: '))
# for num0 in num_list:
#     if num0 > num:
#         bigger+=[num0]
#     elif num0 < num:
#         smaller+=[num0]
#     else:
#         equal+=[num0]

# # 2. 輸出大於 num 的數字有那些(由小到大)
# bigger.sort()
# print('bigger: ')
# for num1 in bigger:
#     print(num1)

# # 3. 輸出小於 num 的數字有哪些(由小到大)
# smaller.sort()
# print('smaller: ')
# for num2 in smaller:
#     print(num2)

# # 4. 輸出等於 num 的數字有幾個
# print('equal_num:',len(equal))

# # 5. 將 smaller、equal、bigger 進行合併，並輸出其結果
# sort_num = smaller+equal+bigger
# print(sort_num)

#Exercise 5
# 請使用者輸入一串資料，並將其存入 mydata 中，透過 for 迴圈與 字典 dictionary 統計 mydata 內的字元各有多少個
# mydata = input('mydata: ')
# dictionary = {}
# for i in mydata:
#     if i not in dictionary:
#         dictionary[i] = 1
#     else:
#         dictionary[i] += 1
# print('dictionary:',dictionary)

#Exercise 6
# 來透過程式求出 f(x) = 3x^4+2x^2-7x+8 的解，x為使用者自訂
# (hint: 先自訂 coef = [3,2,-7,8] expon = [4,2,1,0])
coef = [3,2,-7,8] 
expon = [4,2,1,0]
x = float(input('x: '))
y = 0
for i in range(len(coef)):
    y+=coef[i]*(x**expon[i])
print('f(x):',y)