#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#搜索文档树
find_all( name , attrs , recursive , text , **kwargs )
'''
find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件

name 参数
	name 参数可以查找所有名字为 name 的 tag,字符串对象会被自动忽略掉
传字符串
	最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup 会查找与字符串完整匹配的内容
'''
soup.find_all('b')   #返回[<b>The Dormouse's story</b>]  
soup.find_all('a')	 #返回[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
					 #<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
					 #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] 

#传正则表达式
import re
	#传入正则表达式作为参数,BeautifulSoup会通过正则表达式的match()来匹配内容.
for tag in soup.find_all(re.compile("^b")):   
    print(tag.name)			#输出 body    b

#传列表
	#如果传入列表参数,Beautiful Soup 会将与列表中任一元素匹配的内容返回
soup.find_all(["a", "b"])
#结果
#  [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#传 True
	#True 可以匹配任何值,下面代码查找到所有的 tag,但是不会返回字符串节点  
for tag in soup.find_all(True):
	print(tag.name)
#结果
# html
# head
# title
# body
# p
# b
# p
# a
# a

#传方法
	#如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,
	#如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
	#下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
#将这个方法作为参数传入 find_all() 方法,将得到所有
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were...</p>,
#  <p class="story">...</p>]  

#keyword 参数
	#注意：如果一个指定名字的参数不是搜索内置的参数名,
	#搜索时会把该参数当作指定名字 tag 的属性来搜索,如果包含一个名字为 id 的参数,
	#Beautiful Soup 会搜索每个 tag 的 ”id” 属性
soup.find_all(id='link2')
	#结果
#[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

#如果传入href参数，find_all会搜索每个tag的'href'属性
sou.find_all(href=re.compile('elsie')) 
	#结果
## [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]  

#使用多个指定名字的参数可以同时过滤tag的多个属性
soup.find_all(href=re.compile('elsie'),id='link1')
	#结果不打了，懒。。。

#如果想用class过滤怎么办，class可是python的关键字，那就得加个下划线
soup.find_all('a',class_='sister')


#attrs参数
	#有些tag属性在搜索不能使用，比如html5中的'data.*'属性
data_soup = Beautiful('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")   #这个会报错
	#可以通过find_adll()的attrs参数定义一个字典参数来搜索包含特殊属性的tag
data_soup.find_all(attrs={'data-foo':'value'}) #正确输出

#tetx 参数
	#通过text参数可以搜索文档中的字符串内容。与name参数的可选值一样
	#text接受字符串、正则表达式、列表、True
soup.find_all(text='Elsie')

soup.find_all(text=['Tillie','Elsie','Lacie'])

sou.find_all(text=re.compile('Dormouse'))

#limit 参数
	#find_all()方法返回全部的搜索结构，如果文档树很大，那么搜索会很慢，如果不需要全部结果
	#可以用limit参数限制返回结果的数量，当搜索到结果数量达limit限制就停止搜索
soup.find_all('a',limit=2)

#recursive 参数
	#find_all()会检索当前tag的所有子孙节点，如果只搜索tag的直接子节点可以使用recursive=False

#以下方法参数用法与 find_all() 完全相同，原理均类似
	#find()与find_all()的唯一区别是find_all()返回的是包含一个元素的列表，find()直接返回结果
find(name, attrs, recursive, text, **kwargs)
	
	#find_all()和find()只搜索当前节点的所有子孙节点，find_parents()和find_parent()搜索当前节点的父节点
	#搜索方法与普通的tag搜索方法相同，搜索文档包含的内容
find_parents()  find_parent()

	#这两个方法通过.next_siblings属性对当前tag的所有后面解析的兄弟tag节点进行迭代
	#find_next_siblings返回所有符合的兄弟节点，find_next_sibling只返回后面的第一个tag节点
find_next_siblings() find_next_sibling()

	#这两个方法通过.previous_siblings属性对当前节点前面的tag和字符串进行迭代
	#find_next_siblings返回所有符合的节点，find_next_sibling只返回第一个tag节点
find_previous_siblings() find_previous_sibling()

	#这两个方法通过.netx_elements属性对当前tag之后的tag和字符串进行迭代
	#find_all_next()方法返回所有符合条件的节点，find_next()只返回第一个节点
find_all_next() find_next()

	#这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代
	#find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点
find_all_previous() 和 find_previous()