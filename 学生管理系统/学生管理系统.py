import  os


filename = 'stu_list.txt'
def main():
    while True:
        menu()
        try:
            choice = int(input('请选择'))
        except:
            print('请输入正确类型')
            continue
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'Y' or answer == 'y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息
            else:
                print('输入错误，请重新输入')
        else:
            print('输入错误，请重新输入')

def menu():
        print("=======================数据库==============================")
        print("----------------------------------------------------------")
        print('\t1.录入学生信息')
        print('\t2.查找学生信息')
        print('\t3.删除学生信息')
        print('\t4.修改学生信息')
        print('\t5.排序')
        print('\t6.统计学生总人数')
        print('\t7.显示所有学生信息')
        print('\t0.退出')
        print("----------------------------------------------------------")

def insert():
    student_list = []
    while True:
        id = input("请输入学生学号：")
        if not id:
            break
        name = input("请输入学生姓名:")
        if not name:
            break
        try:
            # 使用int 是为了后期用于排序与运算
            english = int(input("请输入学生英语成绩:"))
            python = int(input("请输入学生Python成绩："))
            java = int(input("请输入学生Java成绩："))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        student = {'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer = input('是否继续添加y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    # 调用save()函数
    save(student_list)

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open('student_list.txt', 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')  # 使用循环遍历 增加了内容的可读性（一行行的对应的内容对应起来，列表包含字典的优势）
      # studentlist.write(str(lst))    # 虽然也可以输出，但是内容只有一行，不经过数处理很难看清楚
    stu_txt.close()

def search():
    while True:
        # print('-----------------------------------------')
        # print("1.按学号搜索")
        # print("2.按姓名搜索")
        # print('-----------------------------------------')
        # choice = int(input("请选择指令："))
        id = input("请输入学号：")
        if id != "":
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    student_old = file.readlines()
            else:
                student_old = []
            if student_old:
                d={}
                for item in student_old:
                    d=dict(eval(item))
                    if d['id'] == id:       # 格式也需要相同，因为一开始把id设置成了int，所以导致type不同
                        print(str(d['id']),str(d['name']),str(d["english"]),str(d['python']),str(d["java"]),"\n")
                    else:
                        continue
            else:
                print("无学生信息")
                break
        else:
            break
        answer = input("是否继续进行搜索?y/n")
        if  answer == "y" or answer == "Y":
            continue
        else:
            break

def delete():
    while True:
        id = input('请输入要删除的学生的id:')
        if id != "":
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()  # 读取学生的数据         # readline 和 readlines 是两个不同的方法
            else:
                student_old = []    # 用于判断为False
            flag = False  # 标记是否删除
            if student_old:     # 上面定义空列表用于判断
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d = dict(eval(item))    # 存储在txt中的文件作为字符串，需要转换回字典才能查询id（eval可去除双引号）
                        if d['id'] != id:
                            wfile.write(str(d)+'\n')    # 存储回txt需要转化回字符串，\n是换行符
                        else:
                            flag = True
                    if flag:
                        print(f'id为{id}的学生已被删除')
                    else:
                        print(f'没有找到ID为{id}的学生信息')
            else:
                print("无学生信息")
                break
        else:
            break
        answer = input("还要继续删除学生吗?y/n")
        if answer == "y" or answer == "Y":
            continue
        else:
            break

def modify():
    while True:
        id = input('请输入学号：')
        if id != "":
            if os.path.exists(filename):
                with open(filename, 'r', encoding="utf-8") as file:
                    student_old = file.readlines()
            else:
                student_old = []
            if student_old:
                with open(filename,'w', encoding="utf-8") as wfile:
                    d = {}
                    for item in student_old:    
                        d = dict(eval(item))
                        if d['id'] == id:
                            sid = input("请输入id")
                            if sid == "":
                                break
                            sname = input("请输入姓名")
                            if sname == "":
                                break
                            try:
                                senglish = int(input("请输入英语成绩"))
                                spython = int(input("请输入python成绩"))
                                sjava = int(input("请输入java成绩"))
                            except:
                                print("输入错误，请输入整数型数据")
                                break
                            sstudent = {"id":sid, "name":sname, "english":senglish, "python":spython, "java":sjava}
                            wfile.write(str(sstudent)+"\n")
                        else:
                            wfile.write(str(d)+"\n") 
            else:
                print("无学生数据")
                break
        else:
            break
        answer = input("是否继续修改?y/n")
        if answer == "y" or answer == "Y":
            continue
        else:
            break


def sort():
    pass

def total():
    pass

def show():
    pass

main()
