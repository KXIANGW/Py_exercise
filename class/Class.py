#Exercise 1
# 建立一個 class Rectangle，Rectangle 中屬性有 width, height，方法有
# isRectangel() 判斷是 width, height 是否可以構成 rectangle
# cal_perimeter() 回傳其周長
# cal_area() 回傳其面積

'''
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def isRectangel(self):
        return self.width>0 and self.height>0
    def cal_perimeter(self):
        return 2*(self.width+self.height)
    def cal_area(self):
        return self.width*self.height

if __name__ == '__main__':
    r1 = Rectangle(2,3)
    if r1.isRectangel():
        print('Width:',r1.width,'Height:',r1.height)
        print('Perimeter:',r1.cal_perimeter())
        print('Area:',r1.cal_area())
    r2 = Rectangle(2,0)
    if not r2.isRectangel():
        print('Width:',r2.width,'Height:',r2.height)
        print('It can not form a rectangel')
'''

#Exercise 2
# 建立一個 class Student，Student 中屬性有 name, id, gender, departures，方法有
# printInfo() 輸出 Student 的 namd, id, gender
# getDepartment() 透過 id 來判斷此學生是哪個學院的
# say(message) 輸出 name say message 

'''
class Student:
    def __init__(self,name,id,gender):
        self.name = name
        self.id = id
        self.gender = gender
        self.departments = {'03':'電乙A','04':'電乙B','05':'電甲A','06':'電甲B','07':'電丙A',
                '08':'機械A','09':'機械B','10':'化材A','11':'化材B','12':'工管A','13':'工管B',
                '14':'資工A','15':'資工B','33':'資工C','16':'資管A','17':'資管B',
                '18':'資傳A（設計組）','20':'資傳B（科技組）','22':'管院A（企管）',
                '23':'管院B（企管）','24':'管院C（財金）','25':'管院D（財金）','26':'管院E（國企）',
                '99':'管院I（國企）','28':'管院F（會計）','29':'應外A','30':'中語A','31':'社政A',
                '32':'藝設A','27':'管院英專G','35':'資訊英專A','36':'人社英專A','37':'電通英專A','38':'工程英專A'}

    def printInfo(self):
        print('Name  ','Id     ','Gender')
        print(self.name, self.id,self.gender)

    def getDepartment(self):
        departmentID = self.id[3:5]
        if departmentID not in self.departments:
            print('Error id!')
            return
        return self.departments[departmentID]

    def say(self,message):
        print(self.name,'says:',message)

if __name__ == '__main__':
    s = Student('兮兮兮','1111111','male')
    s.printInfo()
    print('Department:',s.getDepartment())
    s.say('hihi!')
'''


#Exercise 3
# 建立一個 class Animal，Animal 中屬性有 name, sound, feet，方法有
# printInfo() 輸出 Animal 的 name, feet
# say() 輸出 Animal 的叫聲

'''
class Animal:
    def __init__(self, name,sound,feet):
        self.name = name
        self.sound = sound
        self.feet = feet
    def printInfo(self):
        if self.feet ==0:
            print(self.name,'has no foot')
        elif self.feet ==1:
            print(self.name,'has a foot')
        else:
            print(self.name,'has',self.feet,'feet')
    def say(self):
        print(self.name+': '+self.sound*2)

if __name__ == '__main__':
    cat = Animal('cat','meow',4)
    cat.printInfo()
    cat.say()
    snake = Animal('snake','hiss',0)
    snake.printInfo()
    snake.say()
'''

# Exercise 4
# 建立一個 class ShoppingCart，ShoppingCart 中屬性有 basket(存放購買的物品), info(物品的數量、價格)，方法有
# getAmount() 回傳購物車內有多少商品數量
# getCost() 回傳現在所需花費的金額
# add(thing1,price1) 將物品新增至 basket、info 中
# remove(thing) 移除特定物品
# myBasket() 輸出 basket 內的所有商品


class ShoppingCart:
    def __init__(self,basket,info):
        self.basket = basket
        self.info = info
    def getAmount(self):
        amount = 0
        for i in self.basket:
            amount+=self.info[i][0]
        return amount
    def getCost(self):
        cost = 0
        for i in self.basket:
            cost+=self.info[i][0]*self.info[i][1]
        return cost
    def add(self,thing1,price1):
        if thing1 not in self.basket:
            self.basket.append(thing1)
        if thing1 not in self.info:
            self.info.update({thing1:[1,price1]})
        else:
            self.info[thing1][0]+=1
    def remove(self,thing):
        if thing not in self.basket:
            print(thing,'was not be ordered!')
            return
        self.basket.remove(thing)
        del self.info[thing]
    def myBasket(self):
        for i in self.basket:
            print(i,end = ' ')
        print()

if __name__ == '__main__':
    sc = ShoppingCart(['apple', 'orange','notebook'],
                      {'apple':[2,20], 'orange':[1,25],'notebook':[3,40]})
    sc.myBasket()
    print('Amount:',sc.getAmount())
    print('Cost:',sc.getCost())
    print("\nAdd two pens")
    sc.add('pen',10)
    sc.add('pen',10)
    sc.myBasket()
    print('Amount:',sc.getAmount())
    print('Cost:',sc.getCost())
    print("\nRemove pen")
    sc.remove('pen')
    sc.myBasket()
    print('Amount:',sc.getAmount())
    print('Cost:',sc.getCost())
