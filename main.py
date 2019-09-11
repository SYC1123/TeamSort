import os
from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog
import xlrd
import xlwt
import easygui as g

root = Tk()
root.title("队列排队程序1.0(计软科协：syc)")
root.geometry("500x100")
root.geometry("+500+500")

fup = Frame()
fup.pack()

usernum = StringVar()

lable1 = Label(fup, text="请输入一行的人数", width=8, anchor=E)
lable1.grid(row=1, column=1)
entry1 = Entry(fup, textvariable=usernum, width=20)
entry1.grid(row=1, column=2)


def getFinalandLeft(left_num, people_data):
    '''
    得到分组好的数据和剩余人的数据
    :param left_num: 多余的学生数量
    :param people_data: 学生的原始数据
    :return:多余的学生信息
    '''
    left_people = []  # 多余的学生信息
    for i in range(left_num):
        left_people.append(people_data[i])
        del people_data[i]
    return left_people


def getfinalgroup(people_rows, people_data, row_num):
    '''
    得到最终分组
    :param people_rows: 学生的行数
    :param row_num: 每一行的人数
    :param people_data: 学生数据
    :return: 最终的分组
    '''
    people_final_data = []
    for i in range(int(people_rows)):
        people_final_data.append(people_data[(i * row_num):(row_num * i + row_num)])
    return people_final_data


def grouping(set):
    '''
    一行的人排队
    :param set:一组数据
    :return:排好队的数据
    '''


def xz():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        if usernum.get().isdigit():
            try:
                row_num = int(usernum.get())
                men = {}
                women = {}
                book = xlrd.open_workbook(filename)  # 打开一个excel
                sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
                # sheet2 = book.sheet_by_name('case1_sheet')  # 根据sheet页名字获取sheet
                # 姓名，性别，身高
                print(sheet.cell(0, 0).value)  # 指定行和列获取数据
                print(sheet.cell(0, 1).value)
                print(sheet.cell(0, 2).value)

                print('行' + str(sheet.ncols))  # 获取excel里面有多少列
                print('列' + str(sheet.nrows))  # 获取excel里面有多少行
                # print('获取每一行的数据')
                # for i in sheet.get_rows():
                #     print(i)  # 获取每一行的数据
                # print('获取第一行')
                # print(sheet.row_values(0))  # 获取第一行
                print('获取每一行数据')
                men_num = 1
                women_num = 1
                for i in range(1, sheet.nrows):  # 0 1 2 3 4 5
                    # print(sheet.row_values(i))  # 获取第行的数据
                    if sheet.row_values(i)[1] == 1.0:
                        if sheet.row_values(i)[0] in men.keys():  # 有重名
                            if men[sheet.row_values(i)[0]] != sheet.row_values(i)[2]:  # 姓名相同 身高不同才算重名
                                men.update({sheet.row_values(i)[0] + str(men_num): sheet.row_values(i)[2]})
                                men_num = men_num + 1
                        else:
                            men.update({sheet.row_values(i)[0]: sheet.row_values(i)[2]})
                    else:
                        if sheet.row_values(i)[0] in women.keys():  # 有重名
                            if women[sheet.row_values(i)[0]] != sheet.row_values(i)[2]:  # 姓名相同 身高不同才算重名
                                women.update({sheet.row_values(i)[0] + str(women_num): sheet.row_values(i)[2]})
                                women_num = women_num + 1
                        else:
                            women.update({sheet.row_values(i)[0]: sheet.row_values(i)[2]})
                print(men)
                print(women)
                # print(sheet.col_values(1))  # 取第一列的数据
                # for i in range(sheet.ncols):
                #     print(sheet.col_values(i))  # 获取第几列的数据
                men_data = sorted(men.items(), key=lambda x: x[1])
                women_data = sorted(women.items(), key=lambda x: x[1])
                print("排序好的男生")
                print(men_data)
                print("排序好的女生")
                print(women_data)
                '''
                row_num:一行的人数
                '''

                men_left = []  # 多余的男生信息
                women_left = []  # 多余的女生信息
                men_final_data = []
                women_final_data = []
                men_rows = len(men_data) / row_num  # 男生的行数
                men_left_num = len(men_data) % row_num  # 多余的男生数量
                women_rows = len(women_data) / row_num  # 女生的行数
                women_left_num = len(women_data) % row_num  # 多余的女生数量
                men_left = getFinalandLeft(men_left_num, men_data)
                women_left = getFinalandLeft(women_left_num, women_data)
                print('多余的男生信息')
                print(men_left)
                # print('最终男生信息')
                # print(men_data)
                print('多余的女生信息')
                print(women_left)
                print(len(women_left))
                # print('最终女生生信息')
                # print(women_data)
                men_final_data = getfinalgroup(men_rows, men_data, row_num)
                print('最终男生信息')

                for x in range(len(men_final_data)):
                    output = []
                    if len(men_final_data[x]) % 2 == 0:
                        for i in range(0, len(men_final_data[x]), 2):
                            output.append(men_final_data[x][i])
                        for i in range(len(men_final_data[x]) - 1, 0, -2):
                            output.append(men_final_data[x][i])
                    else:
                        for i in range(0, len(men_final_data[x]), 2):
                            output.append(men_final_data[x][i])
                        for i in range(len(men_final_data[x]) - 2, 0, -2):
                            output.append(men_final_data[x][i])
                    men_final_data[x] = output

                print(men_final_data)
                women_final_data = getfinalgroup(women_rows, women_data, row_num)
                print('最终女生生信息')

                for x in range(len(women_final_data)):
                    output = []
                    if len(women_final_data[x]) % 2 == 0:
                        for i in range(0, len(women_final_data[x]), 2):
                            output.append(women_final_data[x][i])
                        for i in range(len(women_final_data[x]) - 1, 0, -2):
                            output.append(women_final_data[x][i])
                    else:
                        for i in range(0, len(women_final_data[x]), 2):
                            output.append(women_final_data[x][i])
                        for i in range(len(women_final_data[x]) - 2, 0, -2):
                            output.append(women_final_data[x][i])
                    women_final_data[x] = output

                print(women_final_data)
                styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')  # 红色
                # 只能写不能读
                book = xlwt.Workbook()  # 新建一个excel
                sheet = book.add_sheet('最终名单')  # 添加一个sheet页
                row = 0  # 控制行
                for stu in women_final_data:
                    col = 0  # 控制列
                    for s in stu:  # 再循环里面list的值，每一列
                        sheet.write(row, col, str(s[0]) + "(女)", styleBlueBkg)
                        sheet.write(row + 1, col, str(s[1]))
                        col += 1
                    row += 2
                for stu in men_final_data:
                    col = 0  # 控制列
                    for s in stu:  # 再循环里面list的值，每一列
                        sheet.write(row, col, str(s[0]) + "(男)", styleBlueBkg)
                        sheet.write(row + 1, col, str(s[1]))
                        col += 1
                    row += 2

                sheet1 = book.add_sheet('多出的人')  # 添加一个sheet页
                row = 0  # 控制行
                col = 0  # 控制列
                for s in women_left:  # 再循环里面list的值，每一列
                    sheet1.write(row, col, str(s[0]) + "(女)", styleBlueBkg)
                    sheet1.write(row + 1, col, str(s[1]))
                    col += 1
                row += 2
                col = 0  # 控制列
                for s in men_left:  # 再循环里面list的值，每一列
                    sheet1.write(row, col, str(s[0]) + "(男)", styleBlueBkg)
                    sheet1.write(row + 1, col, str(s[1]))
                    col += 1
                row += 2
                book.save(os.path.join(os.path.expanduser('~'), "Desktop") + "\\排队名单.xls")  # 保存到当前目录下
            except:
                showwarning("警告", "您选择的文件格式错误！")
        else:
            showwarning("警告", "请输入合法的整数！")
    else:
        lb.config(text="您没有选择任何文件")


fdown = Frame()
fdown.pack()
lb = Label(fdown, text='')
lb.pack()
btn = Button(fdown, text="选择文件", command=xz)
btn.pack()

mainloop()
