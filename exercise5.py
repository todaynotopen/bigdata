# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:46:41 2018

@author: root
"""
import urllib.request as r 
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
city=input('please input the city name:    ')
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
def tips(a):
    if a=='Clear':
        print('tips:天气晴朗注意防嗮')
    elif a=='Clouds':
        print('tips:阴天何不出去快乐快乐')
    elif a=='Rain':
        print('tips:雨天注意带伞')
def weather(day):
    print('day'+str(day)+':  ')
    t=2+(int(day)-1)*8
    print('tempreture:'+str(data['list'][t]['main']['temp']))
    print('cityname:'+str(data['city']['name']))
    print('description:'+str(data['list'][t]['weather'][0]['description']))
    print('temp_min:'+str(data['list'][t]['main']['temp_min']))
    print('temp_max:'+str(data['list'][t]['main']['temp_max']))
    print('pressure:'+str(data['list'][t]['main']['pressure']))
    tips(str(data['list'][t]['weather'][0]['main']))
for day in range(1,5):
    weather(day)
def chart(day):
    t=2+(int(day)-1)*8
    a='-'*int(data['list'][t]['main']['temp'])
    return a
print('the day line chart is')
for day in range(1,5):
    print(chart(day))
