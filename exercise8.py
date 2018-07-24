# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:10:44 2018

@author: root
"""
f=open('嘉兴.txt','w',encoding='utf-8')
#########抓取数据
import urllib.request as r 
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&ie=utf8&loc=%E5%98%89%E5%85%B4&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&ajax=true&s={}'
'''
def whri(num):
    name=data['mods']['itemlist']['data']['auctions'][num]['raw_title']
    price=data['mods']['itemlist']['data']['auctions'][num]['view_price']
    location=data['mods']['itemlist']['data']['auctions'][num]['item_loc']
    f=open('淘宝数据.csv','a',encoding='utf-8')
    f.write(str(name)+'\t'+str(price)+'\t'+str(location)+'\n')
'''
for page in range (1,101):
    data=r.urlopen(url.format((int(page)-1)*44)).read().decode('utf-8','ignore')
    import json#将字符串转换为字典
    data=json.loads(data)
    f.write(str(data)+'\n')
f.close()
