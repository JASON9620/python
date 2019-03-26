# -*- coding:utf-8 -*-
# this is the function modle
import xlrd


# load data
# str is the path of dta
# this function returns 【【【only the first sheet 】】】
def read_data(str):
	data = xlrd.open_workbook(str)
	table = data.sheets()[0]
	return table


def find_biggest(dict):  # find the biggest number
	temp = ['null', -9999]
	if isinstance(dict,list):
		for i in dict:
			if i[1] > temp[1]:
				temp = i
		return temp
	else:
		for i in dict:
			if dict[i] > temp[1]:
				temp = [i, dict[i]]
		return temp[0]


def top15percent(dict):
	loop = round(len(dict) * 0.15)
	loop = min(15, len(dict))
	temp = []
	for j in range(0, loop):
		i = find_biggest(dict)
		temp.append([i, dict[i]])
		dict.pop(temp[-1][0])
	return temp


# build the function to caculate
# return a a_list that contains the name\model\number\supplier\buyyer\date of every slip
def base_info(info):
	a_list = []
	index = 1
	key = 1
	while key == 1:
		try:
			a_list.append([info.row_values(index)[4], info.row_values(index)[7], info.row_values(index)[11],
						 info.row_values(index)[16], info.row_values(index)[3], info.row_values(index)[1]])
			index = index + 1
		except:
			key = 0
	return a_list


def amount_buyyer_plus(a_list):
	dict1 = {}
	dict2 = {}
	index = 0
	key = 1
	while key == 1:
		try:
			if '公司' in a_list[index][4]:
				if a_list[index][4] in dict1:
					dict1[a_list[index][4]] += a_list[index][2]
				else:
					dict1[a_list[index][4]] = 0
					dict1[a_list[index][4]] += a_list[index][2]
			elif '医院' in a_list[index][4]:
				if a_list[index][4] in dict2:
					dict2[a_list[index][4]] += a_list[index][2]
				else:
					dict2[a_list[index][4]] = 0
					dict2[a_list[index][4]] += a_list[index][2]
			else:
				pass
			index += 1
		except:
			key = 0
	return dict1, dict2


def amount_buyyer_model(a_list):
	dict = {}
	index = 0
	key = 1
	while key == 1:
		try:
			if a_list[index][4] in dict:
				dict[a_list[index][4]].append([a_list[index][1], a_list[index][2]])
			else:
				dict[a_list[index][4]] = []
				dict[a_list[index][4]].append([a_list[index][1], a_list[index][2]])
			index += 1
		except:
			key = 0
	return dict


def amount_buyyer(a_list):
	dict = {}
	index = 0
	key = 1
	while key == 1:
		try:
			if a_list[index][4] in dict:
				dict[a_list[index][4]] += a_list[index][2]
			else:
				dict[a_list[index][4]] = 0
				dict[a_list[index][4]] += a_list[index][2]
			index += 1
		except:
			key = 0
	return dict


# amount of suppiler
def amount_supplier(a_list):
	dict = {}
	index = 0
	key = 1
	while key == 1:
		try:
			if a_list[index][3] in dict:
				dict[a_list[index][3]].append([a_list[index][0], a_list[index][2]])
			else:
				dict[a_list[index][3]] = []
				dict[a_list[index][3]].append([a_list[index][0], a_list[index][2]])
			index = index + 1
		except:
			key = 0
	return dict


# amount of 剂型
def amount_model(a_list):  # this function return a dictionary which structure is model:[name,number]
	dict = {}
	index = 0
	key = 1
	while key == 1:
		try:
			if a_list[index][1] in dict:
				dict[a_list[index][1]].append([a_list[index][0], a_list[index][2]])
			else:
				dict[a_list[index][1]] = []
				dict[a_list[index][1]].append([a_list[index][0], a_list[index][2]])
			index = index + 1
		except:
			key = 0
	return dict


def caculate_number_with_different_supplier(dict):
	temp = []
	for i in dict:
		tt = [i, {}]
		for j in dict[i]:
			if j[0] in tt[1]:
				tt[1][j[0]] += j[1]
			else:
				tt[1][j[0]] = j[1]
		t = 0
		for j in tt[1]:
			t = t + tt[1][j]
		temp.append([tt[0], t])
	return temp


def caculate_number_with_different_model(dict):
	temp = []
	for i in dict:
		tt = [i, {}]
		for j in dict[i]:
			if j[0] in tt[1]:
				tt[1][j[0]] += j[1]
			else:
				tt[1][j[0]] = j[1]
		temp.append(tt)
	return temp


'''



class base_data:
	name=''
	modle=''
	number=0
	supplier=''
	buyyer=''
	def __init__(self,na,mod,numb,suppl,buyy):
		self.name=na 
		self.modle=mod
		self.number=numb
		self.supplier=suppl
		self.buyyer=buyy 
		print ('sucessful')
'''
#***************************************************

#from func import *

#str=input('>>please input the path and name of the data')
str='E:\document\jw\data.xlsx'		#this line is for test

result=read_data(str)	#result is the base information

a_list=base_info(result) 	#obtain the information in a_lists name\model\number\supplier\buyyer\date




#data1 contains the top 15 kind of goods
divided_in_model=amount_model(a_list)
data_in_model_name=caculate_number_with_different_model(divided_in_model)
data1={}	#	{ model : [ [name,number]*n ] }
for i in data_in_model_name:
	data1[i[0]]=top15percent(i[1])

# print (data1)
def data11():
    print (data1)

# data2 contains the top 30 of supplier
divides_in_supplier = amount_supplier(a_list)
data_in_supplier_name = caculate_number_with_different_supplier(divides_in_supplier)
data2 = []  # [ [ supplier , number ]*n ]
loop = 30
for i in range(0, 30):
    a = find_biggest(data_in_supplier_name)
    data2.append(a)
    data_in_supplier_name.remove(a)

# print(data2)
def data22():
    print (data2)

data3 = amount_buyyer(a_list)
temp = []
for i in range(0, 30):
    temp.append([find_biggest(data3), data3[find_biggest(data3)]])
    data3.pop(find_biggest(data3))
data3 = temp
# print(data3)
def data33():
    print (data3)


data4, data5 = amount_buyyer_plus(a_list)  # data4,data5 分别是客户为公司和医院分类前30名
t1 = []
t2 = []
for i in range(0, 20):
    t1.append([find_biggest(data4), data4[find_biggest(data4)]])
    data4.pop(find_biggest(data4))
    t2.append([find_biggest(data5), data5[find_biggest(data5)]])
    data5.pop(find_biggest(data5))
data4 = t1
data5 = t2
def data44():
    for i in data4:
        print(i)
def data55():
    for i in data5:
        print(i)
# for i in data4:
#     print(i)
# for i in data5:
#     print(i)

data66 = amount_buyyer_model(a_list)
data6 = amount_buyyer(a_list)
temp = []
for i in range(0, round(len(data6) * 0.5)):
    temp.append([find_biggest(data6), data6[find_biggest(data6)]])
    data6.pop(find_biggest(data6))
data6 = temp
temp = []
for i in data6:
    temp.append([i[0], {}])
    for j in data66[i[0]]:
        if j[0] in temp[-1][1]:
            temp[-1][1][j[0]] += j[1]
        else:
            temp[-1][1][j[0]] = j[1]
data6 = temp
# print(data6)
def data66():
    print (data6)



#	attention!!!	this part is based on data1
temp = {}
l = []
for i in range(0, 19):
    l.append(0)
for i in data1:
    temp[i] = {}
    for j in data1[i]:
        temp[i][j[0]] = l

for i in a_list:
    if i[1] in temp:
        if i[0] in temp[i[1]]:
            temp[i[1]][i[0]][(int(i[5][3]) - 7) * 11 + int(i[5][5:7]) - 1] += i[2]

data7 = temp
# print(data7)
def data77():
    print (data7)


#	attention!!!	this part is based on data4 and data5
t1 = {}
t2 = {}
l = []
for i in range(0, 19):
    l.append(0)
for i in data4:
    t1[i[0]] = l

for i in data5:
    t2[i[0]] = l

for i in a_list:
    if i[4] in t1:
        t1[i[4]][(int(i[5][3]) - 7) * 11 + int(i[5][5:7]) - 1] += i[2]
    if i[4] in t2:
        t2[i[4]][(int(i[5][3]) - 7) * 11 + int(i[5][5:7]) - 1] += i[2]
# for i in t2:
#     # print(i, t2[i])
# for i in t1:
#     # print(i, t1[i])
def data88():
    for i in t2:
        print(i,t2[i])
def data99():
    for i in t1:
        print(i,t1[i])


from tkinter import *


root = Tk()
root.geometry("300x450")
root.title("Chengyu Data")

root.update()

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="各剂型销售前15", fg="blue",font="Helvetica -12 bold", command=data11, width = 20, height = 2)
        self.button.pack()

        self.hi_there = Button(
            frame, text="供应商前30",fg="blue",font="Helvetica -12 bold", command=data22,width = 20, height = 2)
        self.hi_there.pack()
        self.hi_there1 = Button(
            frame, text="客户销售前30", fg="blue", font="Helvetica -12 bold", command=data33, width=20, height=2)
        self.hi_there1.pack()
        self.hi_there2 = Button(
            frame, text="公司销售前30", fg="blue", font="Helvetica -12 bold", command=data44, width=20, height=2)
        self.hi_there2.pack()
        self.hi_there3 = Button(
            frame, text="医院销售前30", fg="blue", font="Helvetica -12 bold", command=data55, width=20, height=2)
        self.hi_there3.pack()
        self.hi_there4 = Button(
            frame, text="客户前50%大品种占比量", fg="blue", font="Helvetica -12 bold", command=data66, width=20, height=2)
        self.hi_there4.pack()
        self.hi_there7 = Button(
            frame, text="各剂型前15月环比", fg="blue", font="Helvetica -12 bold", command=data77, width=20, height=2)
        self.hi_there7.pack()
        self.hi_there8 = Button(
            frame, text="销售前20医院月环比", fg="blue", font="Helvetica -12 bold", command=data88, width=20, height=2)
        self.hi_there8.pack()
        self.hi_there9 = Button(
            frame, text="销售前20公司月环比", fg="blue", font="Helvetica -12 bold", command=data99, width=20, height=2)
        self.hi_there9.pack()






app = App(root)

root.mainloop()