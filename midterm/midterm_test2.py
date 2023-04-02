# Exercise 2
# 實作一個成績系統，自訂一個 user_name = {account_number:'', password:'',一上:[]}
# 而此系統有兩種功能，選擇(1) 修改資料 (2) 獲取資料...
# 修改資料內有 1. 更改密碼(需再輸入一次密碼) 2. 添加/修改一個學期的成績(格式: 學期 課名 成績)...
# 獲取資料內有 1. 哪幾個學期的成績(格式: 一上、二下)...
user = {'account_number':'1110000', 'password':'password',
        '一上':['Chinese(I)', '84', 'Calculus(I)', '99', 'English(I)', '88']}
a = 1
while a:
    account_number = input("Input account number: ")
    if account_number == user['account_number']:
        password = input("Input password: ")
        if password == user['password'] :
            choice = input("Input your choice: (1) Modify data (2) Get data: ")
            if choice == '1':
                choice2 = input("1. Change password 2. Add/modify grades for one semester: ")
                if choice2 == '1':
                    password = input("Input password: ")
                    if password == user['password'] :
                        new_password = input("Input new password: ")
                        user['password'] = new_password
                        print(user)
                    else:
                        print("Error password")
                elif choice2 == '2':
                    semester = input('Add the grades for one semester: ')
                    semester = semester.split(' ')
                    course_grade = semester[1:]
                    semester = semester[0]
                    user.update({semester:course_grade})
                    print(user)
                else:
                    print('Oh oh, something bad happened')                  
            elif choice == '2':
                get_semester = input("Which semester(s): ")
                get_semester = get_semester.split('、')
                semester_num = len(get_semester)
                # 最多四個學期，因此做多判斷四次
                print('user')
                if semester_num > 4:
                    print('Oh oh, something bad happened')
                else:
                    if semester_num>0 :
                        semester = get_semester[semester_num-1]
                        if semester in user:
                            print(semester, ' ' .join(user[semester]))
                        semester_num-=1
                    if semester_num>0 :
                        semester = get_semester[semester_num-1]
                        if semester in user:
                            print(semester, ' ' .join(user[semester]))
                        semester_num-=1
                    if semester_num>0 :
                        semester = get_semester[semester_num-1]
                        if semester in user:
                            print(semester, ' ' .join(user[semester]))
                        semester_num-=1
                    if semester_num>0 :
                        semester = get_semester[semester_num-1]
                        if semester in user:
                            print(semester, ' ' .join(user[semester]))
                        semester_num-=1
                    print()
            else:
                print('Oh oh, something bad happened')
        else:
            print("Error password")
    else:
        print("Error account number!")


