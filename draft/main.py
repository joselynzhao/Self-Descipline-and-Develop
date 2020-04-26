#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:main.py
@TIME:2020/4/26 19:49
@DES: 自律 ` 自我养成类管理
'''
import os
import os.path as osp
import codecs

class ITEM:
    def __init__(self,name,time,cycle):
        self.name = name
        self.time = time
        self.cycle = cycle    #[day,week,month]
        self.remain = self.time
    def update_1(self):
        self.remain-=1



class DESCIPLINE:
    def __init__(self):  # 用文件当数据库
        self.item_list = []
        self.__recover_data__()
        self.score = 0

    def __new_update__(self,cycle): # 先手动操作吧
        for item in self.item_list:
            if item.cycle is cycle:
                item.remain = item.time
    def new_day(self):
        self.__new_update__('day')
    def new_week(self):
        self.__new_update__('week')

    def __recover_data__(self): # 恢复文件内部的数据
        if osp.exists('user_data.txt'):
            data_file = codecs.open('user_data.txt','r','utf-8')
            info = data_file.readlines()
            for line in info:
                name,time,cycle = line.strip().split('^')
                self.item_list.append(ITEM(name,time,cycle)) #注意这里获取的数据类型都是 str
            print("The data is loaded")
        else:
            print("welcome to use SDD")
    def __storage__(self):  #退出程序的时候执行
        data_file = codecs.open('user_data.txt','w')
        for item in self.item_list:
            data_file.write('{}^{}^{}\n'.format(item.name,item.time,item.cycle))
    def exit(self):
        self.__storage__()
        print('good bye')
    def add_item(self):
        name = input("please input item name")
        time = input("please input item times")
        cycle = input("please input item cycle(1:day,2:week,3:month)")
        self.item_list.append(ITEM(name,time,cycle))
        self.__storage__()
    def delete_item(self):
        name = input("please input item name you want delete")
        for item in self.item_list:
            print(item.name)
            if item.name == name:
                self.item_list.remove(item)
                print('the item named \'{}\' is deleted'.format(name))
        self.__storage__()
    def modify_item(self):
        name = input("please input item name you want modify")
        attr,content = input('please input the attribution and content(eg:time,2)').split()  #输入格式非常容易报错
        for i in range(len(self.item_list)):
            item = self.item_list[i]
            if item.name == name:
                if attr == 'name':
                    self.item_list[i].name=content
                elif attr == 'time':
                    self.item_list[i].time = content
                elif attr == 'cycle':
                    self.item_list[i].cycle = content
                else:
                    print('input error!')
                    return
        print("modify over")
        self.__storage__()
    def show_items(self):
        # sorted(self.item_list,key=   ('cycle','time'))
        for item in self.item_list:
            print('{}: {}/{} per {}'.format(item.name,item.remain,item.time,item.cycle))


if __name__=='__main__':
    descipline = DESCIPLINE()
    out_app = 0
    while(not out_app):
        print('1：add item')
        print('2：delete item')
        print('3：modify item')
        print('4：show items')
        print('0: exit')
        order = input("please input your choose")
        if order is '1':
            descipline.add_item()
        elif order is '2':
            descipline.delete_item()
        elif order is '3':
            descipline.modify_item()
        elif order is '4':
            descipline.show_items()
        elif order is '0':
            descipline.exit()








