# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:35:00 2018
练习6：
1.显示4个商品然后分割，只要第一页36个商品信息
2.列出36商品
3.获取所有的商品价格并且给商品排序，从高到低排序
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示。
@author: root
"""
import urllib.request as r 
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'
page=input('please input the page    ')
data=r.urlopen(url.format((int(page)-1)*44)).read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
def info(num):
    name=data['mods']['itemlist']['data']['auctions'][num]['raw_title']
    price=data['mods']['itemlist']['data']['auctions'][num]['view_price']
    location=data['mods']['itemlist']['data']['auctions'][num]['item_loc']
    print('商品名称：'+str(name)+'\n商品价格:'+str(price)+'\n出货地点:'+str(location))
print('显示四个商品')
for num in range(0,4):
    print('第'+str(num+1)+'件商品：')
    info(num)
    print('-'*30)
def goods(num):
    return data['mods']['itemlist']['data']['auctions'][num]['raw_title']
for num in range(0,36):
    print('第'+str(num+1)+'件商品：'+goods(num))
print('-'*30)
##########3
def price(num):
    return float(data['mods']['itemlist']['data']['auctions'][num]['view_price'])
pri=[]
for num in range(0,36):
    pri.append(price(num))
print('商品价格排序：')
pri=sorted(pri)
m=reversed(pri)
print(list(m))
##########4
def sale(num):
    p=str(data['mods']['itemlist']['data']['auctions'][num]['view_sales'])
    p=p[0:-3]
    return int(p)
list=[]
for num in range(0,36):
    list.append(sale(num))
print('销量排序：')
print(sorted(list))
###########5
def isfee(num):
    return float(data['mods']['itemlist']['data']['auctions'][num]['view_fee'])
for num in range(0,36):
    if isfee(num)==0:
         info(num) 
    