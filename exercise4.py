# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:45:20 2018
练习题4：
1.打印每天18点的天气信息，温度，城市，情况，气压，最高温度，最低温度
2.写出英文版的天气APP-天气情况，用户输入英文
3.打印温度折线图
（字符的扩展功能，一-表示一度）
4.获取所有温度，并且排序（sorted([1,4,-1,8])#######使用此方法排序
全球5天天气
@author: root
"""

import urllib.request as r #导入梁王工具包，名为r
q=input('please input the address:  ')
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+q+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json#将字符串转换为字典
data=json.loads(data)
print('the first day')
print('tempreture:'+str(data['list'][2]['main']['temp']))
print('cityname:'+str(data['city']['name']))
print('description:'+str(data['list'][2]['weather'][0]['description']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('the second day')
print('tempreture:'+str(data['list'][10]['main']['temp']))
print('cityname:'+str(data['city']['name']))
print('description:'+str(data['list'][10]['weather'][0]['description']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('the third day')
print('tempreture:'+str(data['list'][18]['main']['temp']))
print('cityname:'+str(data['city']['name']))
print('description:'+str(data['list'][18]['weather'][0]['description']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('the fourth day')
print('tempreture:'+str(data['list'][26]['main']['temp']))
print('cityname:'+str(data['city']['name']))
print('description:'+str(data['list'][26]['weather'][0]['description']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('the fifth day')
print('tempreture:'+str(data['list'][34]['main']['temp']))
print('cityname:'+str(data['city']['name']))
print('description:'+str(data['list'][34]['weather'][0]['description']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
a='-'*int(data['list'][2]['main']['temp'])
b='-'*int(data['list'][10]['main']['temp'])
c='-'*int(data['list'][18]['main']['temp'])
d='-'*int(data['list'][26]['main']['temp'])
e='-'*int(data['list'][34]['main']['temp'])
print('the line chart is')
print(a)
print(b)
print(c)
print(d)
print(e)
fd=data['list'][2]['main']['temp']
sd=data['list'][10]['main']['temp']
td=data['list'][18]['main']['temp']
fd=data['list'][34]['main']['temp']
fifd=data['list'][34]['main']['temp']
print('the sorted tempreture is:')
print(sorted([fd,sd,td,fd,fifd]))
