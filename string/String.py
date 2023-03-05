#Exercise 1
num1,num2 = 10,2

#12
sum = num1+num2
print(sum)

#1024
power = num2**num1
print(power)

#102
str_sum = str(num1)+str(num2)
print(str_sum)



#Exercise 2
my_str = "i like python!"

# (1) 請輸出my_str的長度
print(len(my_str))

# (2) 將 my_str 改為 "I like python!"，並輸出 (hint: capitalize())
my_str = my_str.capitalize()
print(my_str)

# (3) 將 my_str 改為 "I really like python!"，並輸出
my_str = my_str.replace("like","really like")

# (4) 透過 " " 將 my_str 進行分割，並將結果存進 str_split 後輸出
str_split = my_str.split(" ")
print(str_split)

# (5) 透過 "-" 將分割結果 str_split 進行合併，並將結果存進new_str 後輸出
new_str = "-".join(str_split)
print(new_str)


#Exercise 3
# 定義一個字串 tag = '<a href="http://www.yzu.edu.tw">'
tag = '<a href="http://www.yzu.edu.tw">'

# (1) 將 tag 中的 yzu 網址存進 link 後輸出
link = tag[9:-2]
print(link)

# (2) 透過 "." 將 link 進行分割，並將結果存進 link_split 後輸出
link_split = link.split(".")
print(link_split)

# (3) 將 link 中的 yzu 改為 ntu，並將結果存進 ntu_link 後輸出
ntu_link = link.replace("yzu","ntu")
print(ntu_link)

# (4) 透過 ntu_link 輸出 "ntu web: http://www.yzu.edu.tw"
ntu_info = "ntu web: "+ntu_link
print(ntu_info)


# Exercise #4
# 請先定義一個字串 box = "apple, waterlemon, lemon, pineapple, wax apple"
box = "apple, waterlemon, lemon, pineapple, wax apple"

# (1) box 內多少顆 apple
print(box.count("apple"))

# (2) 找出 box 內 第一顆 apple 的位置
print(box.find("apple"))

# (3) 找出 box 內 最後一顆 lemon 的位置
print(box.rfind("lemon"))

# (4) 試著將 box 內的水果單字改為大寫
box = box.upper()
print(box)