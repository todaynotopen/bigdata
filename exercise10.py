# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 16:49:21 2018

@author: root
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}
f=open('西藏理科招生.txt','a',encoding='utf-8')
ls=open('all_school.txt',encoding='utf-8').readlines()
id=[]
j=0
for line in ls:
    #print(line.split('-jianjie-')[1].split('.')[0])
    id.append(line.split('-jianjie-')[1].split('.')[0])#获取学校ID
while j<2300:
    print('第{}所学校'.format(j+1))
    req=r.Request(url,data='id={}&type=2&city=50&state=1'.format(id[j]).encode(),headers=headers)
    data=r.urlopen(req).read().decode('utf-8','ignore')
    if data.find('<')!=-1:
        continue
    f.write(data+'\n')
    j=j+1
f.close()
