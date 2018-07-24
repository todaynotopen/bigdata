# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:12:00 2018

@author: root
"""
"""
print('fuck')
ls=open('学校招收人数.txt',encoding='utf-8')
lsLsit = ls.readlines()
print('老哥')
for line in lsLsit:
    print('老哥')
    #print(line.split('(')[1].split(',')[0]+'哪里跑')
    #id.append(line.split('-jianjie-')[1].split('.')[0])#获取
"""
ls=open('学校招收人数.txt',encoding='utf-8').readlines()
f=open('学校.txt','a',encoding='utf-8')
g=open('人数.txt','a',encoding='utf-8')
sc=[]
data=[]
for line in ls:
    sc.append(str(line.split('(')[1].split(',')[0]))
    data.append(int(line.split(',')[1].split(')')[0]))
f.write(str(sc))
g.write(str(data))
f.close()
g.close()