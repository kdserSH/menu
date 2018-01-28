#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Mario Gong
menu = {
    '上海':{
        '黄浦':{
            '人民广场':['博物馆',' 大世界'],
            '南京东路':['步行街','外滩']
        },
        '浦东':{
            '张江':['长泰广场','浦东软件园'],
            '陆家嘴':['国金中心','金茂大厦']
        },
        '杨浦':{
            '五角场':['复旦大学','同济大学'],
            '江湾镇':['江湾体育场','居民区']
        }
    },
    '江苏':{
        '无锡':{},
        '苏州':{},
        '南京':{}
    },
    '浙江':{
        '杭州':{},
        '宁波':{},
        '温州':{}
    }
}
#exit_Flag= False
while True:
    for i in menu:
        print(i)
    choice= input('please in put your choice》》1')
    while True:
        for i2 in menu[choice]:
            print(i2)
        choice2=input('please in put your choice》》2,press b to backup or q to quit')
        if choice2 =='b':
            break
        elif choice2=='q':
            exit()
        while True:
            for i3 in menu[choice][choice2]:
                print(i3)
            choice3 = input('please in put your choice》》2,press b to backup or q to quit')
            if choice3 == 'b':
                break
            elif choice3 == 'q':
                exit()
            for i4 in menu[choice][choice2][choice3]:
                print(i4)
            choice4=input('this is the bottom,press b to backup or q to quit')
            if choice4 == 'b':
                break
            elif choice4=='q':
                exit()