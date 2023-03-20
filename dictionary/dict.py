#Exercise 1

num1 = ["zero", "one", "two", "three", "four", "five", "six"]
num2 = {'0':"zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six"}

# (1) 請輸出 num1、num2 的資料型態
print("num1:", type(num1))
print("num2", type(num2))

# (2) 請輸出 num1 的 "zero" 到 "three"
print(num1[0], num1[1], num1[2], num1[3])

# (3) 請輸出 num2 的 "four" 到 "six"
print(num2['4'], num2['5'], num2['6'])

# (4) 請透過 get() 輸出num2 的 'one'
print(num2.get('1'))




#Exercise 2
box = {"apple":1, "waterlemon":3, "lemon":2, "pineapple":2, "wax apple":5}

# (1) box 內有多少顆 apple、pineapple、wax apple
print("apple_quantity:", box["apple"])
print("pineapple_quantity:", box["pineapple"])
print("wax apple_quantity:", box["wax apple"])

# (2) box 內總共有多少顆水果
sum = box["apple"] + box["pineapple"] + box["wax apple"] + box["waterlemon"] + box["lemon"]
print("Sum:", sum)

# (3) box 中的蘋果被吃掉了一顆，並輸出結果
box["apple"]-=1
print(box)

# (4) 蘋果數量為零了，請將蘋果從 box 中移除
del box["apple"]
print(box)

# (5) 定義一個 favorite_fruit = {fruit_name, fruit_quantity}，並將其存進 box 中
favorite_fruit = {"pear":88}
box.update(favorite_fruit)
print(box)




#Exercise 3
student = {}

# (1) 請將 score = {"Chinese":60} 存進 studnet 內
score = {"Chinese":60}
student.update(score)
print(student)

# (2) 請自行定義一個字典，並將其存放的成績存進student
student.update({"English":85,"Calculus":95})
print(student)

# (3) 將 Chinese 的分數改為 90
student["Chinese"] = 90
print(student)

# (4) 學期結束了，請將student內的成績清空
student.clear()
print(student)




#Exercise 4
import random
encode_text = {}
text = "python is great!bad"
text = list(set(text))
print(text)
num = 16
for i in range(num):
    ch = chr(random.randint(0,127))
    while(ch in encode_text):
        ch = chr(random.randint(0,127))
    encode_text.update({ch: text[i]})
print(encode_text)
encode_text = {'#': 'n', 'R': 'y', 'M': '!', 't': 'd', 'I': 't', '@': 'o', 'h': 'r', 'J': 'i', '_': 'h', '/': 'b', '1': 's', 'r': 'g', '/': 'e', '&': 'p', 'a': ' ', 'b': 'a', '$':'d'}
for i in encode_text.keys():
    print(i,end = ' ')
print()
for i in encode_text.values():
    print(i,end = ' ')
print()
# (1) 請依序將 encode_text 內的 '&','R','I','_','@','#','a','J','1','a' 所對應的值存進 text 
text = encode_text['&']+encode_text['R']+encode_text['I']+encode_text['_']+encode_text['@']+encode_text['#']+encode_text['a']+encode_text['J']+encode_text['1']+encode_text['a']
print(text)

# (2) 請定義一個字串 adj(從 encode 中現有的字母構成)
adj = encode_text['r']+encode_text['h']+encode_text['/']+encode_text['b']+encode_text['I']
print(adj)

# (3) 透過 text 與 adj 輸出一段完整的句子
text = text+adj
print(text)
