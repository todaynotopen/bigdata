# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:08:10 2018
1.加载网络数据(不是重点 只需要记住)
2.解析字典数据
练习题3：
1.通过复制天气代码，获取老家的天气字典
2.打印温度temp，天气情况description， 天气气压 pressure
@author: root
"""
a=b'1' #byte类型
import urllib.request as r  #导入联网工具包  打开网址 读取内容转换为str
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json#字符串转字典工具包
data=json.loads(data)
#字典--->>main字典->temp变量
print(data['main']['temp'])
#data字典-》》wind字典-->speed
print(data['weather'][0]['description'])
print(data['main']['pressure'])