#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup 

#创建 beautifulsoup 对象
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
''' 
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())       #prettify()格式化打印出了它的内容，这个函数经常用到
	'''
	Beautiful Soup 将复杂HTML文档转换成一个复杂的树形结构,每个节点都是 Python 对象,所有对象可以归纳为4种
	Tag
	NavigableString
	BeautifulSoup
	Comment
	'''

# Tag   HTML 中的标签
	'''
	<title>The Dormouse's story</title>
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>  
	'''
	#上面的 title a 等等 HTML 标签加上里面包括的内容就是 Tag，怎样用 Beautiful Soup 来方便地获取 Tags
print(soup.title)
print(soup.head)
	
	#tag有两个重要的属性，是 name 和 attrs
print(soup.name)     #soup 对象本身比较特殊，它的 name 即为 [document]
print(soup.head.name) #对于其他内部标签，输出的值便为标签本身的名称
print(soup.p.attrs)  # p 标签的所有属性打印输出了出来，得到一个字典
	
	#如果我们想要单独获取某个属性,例如我们获取它的 class 叫什么
print(soup.p['class'])   #等价的还有print(soup.p.get('class'))


#NavigableString 既然我们已经得到了标签的内容，那么我们要想获取标签内部的文字用 .string 即可
print(soup.p.string)

#BeautifulSoup BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把当作一个特殊的 Tag
	#分别获取它的类型，名称，以及属性看一下
print(type(soup.name))
print(soup.name)
print(soup.attrs)

#Comment Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号
	#但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦
print(soup.a)
print(soup.a.string)
print(type(soup.a.string)) 
