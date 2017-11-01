#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36'
}
url_all = 'http://pythonscraping.com/pages/warandpeace.html'
html = urlopen(url_all)
soup_1 = BeautifulSoup(html,"lxml")  #把内容传给BeautifulSoup，会按标签转换成结构，如下面
'''
html --->  <html><head>...</head></html>
---head---><head><title>我是title</title></head>
------title---><title>我是title</title>
---body---><body><h1>我是h1</h1>
<div>我是div里的内容</div></body>
------h1---><h1>我是h1</h1>
------div---><div>我是div</div>
可以看出从网页提取的<h1>嵌在BeautifulSoup对象 soup_1 结构第二层html-->body--->h1
但我们可以直接调用如下调用
'''
h1 = soup_1.h1
#假设的我们要抓取内容在所有的<span class='red'></span>标签中,可以这么写
soup_list = soup_1.findAll('span',{'class':'red'})
for i in soup_list:
    print(i.get_text())  #我们提取出来的soup_list是包含标签的，get_text()能去掉这些标签
'''
find()和findAll()
官方文档是这么定义的
findAll(tag, attributes, recursive, text, limit, keyword)
find(tag, attributes, recursive, text, keyword)
我们在99%的时候都只需要tag, attributes,
'''
#tag 可以传一个标签或多个标签组成的序列,下面代码将返回文档当中所有有标题标签的列表

soup_1.findAll({'h1','h2','h3','h4'})

#attributes 传一个封装在字典的一个标签的若干属性和对应的属性值，下面代码会返回所有grenn和red
soup_1.findAll('span',{'class':{'grenn','red'}})

#text 传一段文本内容，返回的是包含该文本的标签数量
soup_1.findAll(text='我就是那段文本')

#limit 范围限制(这个find没有)，如果只需要前几项，可以设置它
soup_1.findAll(limit=4)

#keyword 可以指定那些具有指定属性的标签
soup_1.findAll(id='text') #如果属性是class要加下划线变成class_

#加上测试写了一个小时了，休息一下