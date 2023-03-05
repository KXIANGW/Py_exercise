'''
#Exerciser 1
my_str = "i LIKE PYTHON!"

# (1) 將 my_str 改為 "I like python!" 
my_str = my_str.swapcase()
print(my_str)

# (2) 透過 " " 將 my_str 進行分割，並將結果存進 my_list 後輸出
my_list = my_str.split(" ")
print(my_list)

# (3) 透過分割後的 my_list 輸出 "python! great!" 
print(my_list[2], "great!")

# (4) 將 my_list 改為 ['Everyone', 'likes', 'python!']
my_list[0] = "Everyone"
my_list[1] = "likes"
print(my_list)

# (5) 透過 my_list 將 my_str 改為 "Everyone likes python!"
my_str = " ".join(my_list)
print(my_str)
'''


'''
#Exercise 2
word = input("Pls input your word: ")

# (1) 請將 word 轉為 list 並判斷 word 中有多少英文字母
word = list(word)
print(len(word))

# (2) word 中有沒有 'a' 字母(True/False)
print('a' in word)

# (3) 輸出 word 中開頭、結尾的英文字母
print(word[0], word[-1])

# (4) 透過 [] 將你的 word 改為新的單字
word[0:2] = ["ha"]
word = ''.join(word)
print(word)
'''


'''
#Exercise 3
info = ["Ted", "student", 18, "1120000", ["Dad", "Mom", "Dog"]]

# (1) 請將 info 內 "Ted", 18, "1120000 的索引值存到 name_index, age_index, id_index
name_index = info.index("Ted")
age_index = info.index(18)
id_index = info.index("1120000")
print(name_index, age_index, id_index)

# (2) 透過 name_index, age_index, id_index 與手動輸入個人資訊，將 info 內的資訊進行該改
info[name_index] = input("Pls input your name: ")
info[age_index] = int(input("Pls input your age: "))
info[id_index] = input("Pls input your id: ")
print(info)

# (3) 請輸出 info 內有多少個資訊
print(len(info))

# (4) 請輸出有幾個家庭成員
print(len(info[-1]))

# (5) 家庭成員中有沒有 "sister"(True/False)
print("sister" in info[-1])
'''


'''
#Exercise 4
apple = ['a', 'p', 'p', 'l', 'e']
pen = ['p', 'e', 'n']

# (1) 將 apple、pen 結合再一起並存進 applepen_alphabet
applepen_alphabet = apple+pen
print(applepen_alphabet)

# (2) 透過 '' 將 applepen_alphabet 合併，並存進 applepen 
applepen = ''.join(applepen_alphabet)
print(applepen)

# (3) 透過 applepen 輸出 "I have a applepen"
text = "I have a "+applepen
print(text)
'''


'''
#Exercise 5
empty = list()

# (1) 使用者輸入兩個點座標(格式:x,y)，將其放入空串列中
point1 = input("Point1: ")
point2 = input("Point2: ")
point1 = point1.split(',')
point2 = point2.split(',')

empty.append(point1)
empty.append(point2)
print(empty)

# (2) 求兩端點之距離 (hint: float())
diff_X = float(empty[1][0]) - float(empty[0][0])
diff_Y = float(empty[1][1]) - float(empty[0][1])
length = ((diff_X)**2+(diff_Y)**2)**0.5
print(length)
'''

'''
#Exercise 6
box = "APPLE,WATERLEMON,WAX APPLE,LEMON,PINEAPPLE"

# (1) 將 box 內的水果轉為小寫，並存進 box 後輸出
box = box.lower()
print(box)

# (2) 透過 "," 將 box 分割，並將結果存進 box 後輸出
box = box.split(',')
print(box)

# (3) 輸出 box 內有多少種水果
print("水果數量:", len(box))

# (4) inner_bag = ["guava"], bag = ["banana","orange"]，將 inner_bag 放入 bag 中，再將 bag 的水果放入 box
inner_bag = ["guava"]
bag = ["banana","orange"]
bag.append(inner_bag)
print("bag:", bag)

box.extend(bag)
print("box:", box)

# (5) 將 inner_bag 從 box 中拿掉
box.remove(inner_bag)
print(box)

# (6) box 中是否有 "guava"(True/False)
print("guava" in box)
'''


#Exercise 7
num = [3, 1, 6, 8, 9, 2, 5, 4, 5, 7, 5]

# (1) 輸入你最愛的數字，並插進 num 中第一個位置
favorite_num = int(input("My favorite number: "))
num.insert(0,favorite_num)

# (2) 計算 num 中有幾個 5
print(num.count(5))

# (3) 將 num 由小到大排序，並存在 num_sorted1
num_sorted1 = sorted(num)
print("num_sorted1:", num_sorted1)

# (4) 將 num 由大到小排序，並存在 num_sorted2
num_sorted2 = sorted(num, reverse = True)
print("num_sorted2:",num_sorted2)

# (5) 將 num 本身由小到大排序
num.sort()
print("num:",num)
# (6) 將 num 本身由大到小排序
num.sort(reverse = True)
print("num:",num)
