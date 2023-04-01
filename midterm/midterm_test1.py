# Exercise 1
# 求面積與周長(以下範例只包括圓形、長方形、三角形)
# function 1. 新增一個圖形，接者輸入該圖形的長度(格式: 5,3,4)
# function 2. 求周長
# function 3. 刪除圖形
import math
PI = math.pi
data = {'circle':5,'triangle':[5,3,4]}
a = 1
while a :
    choice = int(input('Input your choice: 1. Add a new shape 2. Calculate the perimeter 3. Delete the shape: '))
    if choice == 1:
        shape = input('Input shape: ')
        if shape == 'circle':
            r = float(input('r: '))
            if r>0:
                data.update({shape:r})
                print(data)
            else:
                print('Cannot form a circle')
        elif shape == 'triangle':
            triangle_len = [float(input('a: ')),float(input('b: ')),float(input('c: '))]
            triangle_len.sort()
            if triangle_len[0]+triangle_len[1]>triangle_len[2]:
                data.update({shape:triangle_len})
                print(data)
            else:
                print("Cannot form a triangle")
        elif shape == 'rectangle':
            rectangle_len = [float(input('x: ')),float(input('y: '))]
            rectangle_len.sort()
            if rectangle_len[0]>0 and rectangle_len[1]>0 :
                data.update({shape:rectangle_len})
                print(data)
            else:
                print("Cannot form a rectangle")
        else:
            print('Oh oh, something bad happened')

    elif choice == 2:
        shape = input('Input shape: ')
        if shape == 'circle':
            if shape in data:
                print('The perimeter of cirlce: ',2*PI*data[shape])
            else:
                print('Oh oh, something bad happened')
        elif shape == 'triangle':
            if shape in data:
                len = data[shape]
                print('The perimeter of triangle: ',len[0]+len[1]+len[2])
            else:
                print('Oh oh, something bad happened')
        elif shape == 'rectangle':
            if shape in data:
                print('The perimeter of rectangle: ',2*(data[shape][0]+data[shape][1]))
            else:
                print('Oh oh, something bad happened')
        else:
            print('Oh oh, something bad happened')

    elif choice == 3:
        shape = input('Input shape: ')
        if shape == 'circle':
            if shape in data:
                del data[shape]
                print(data)
            else:
                print('Oh oh, something bad happened')
        elif shape == 'triangle':
            if shape in data:
                del data[shape]
                print(data)
            else:
                print('Oh oh, something bad happened')
        elif shape == 'rectangle':
            if shape in data:
                del data[shape]
                print(data)
            else:
                print('Oh oh, something bad happened')
        else:
            print('Oh oh, something bad happened')
    else:
        print('Oh oh, something bad happened')
    a = int(input('a: '))
