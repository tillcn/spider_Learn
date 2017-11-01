#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

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

#直接子节点    要点：.contents .children 属性

	#.contents  tag 的 .content 属性可以将tag的子节点以列表的方式输出
print(soup.head.contents)
print(soup.head.contents[0]) #既然是列表，我们当然可以用下标来取某个元素

	#.children  它返回的不是一个 list，不过我们可以通过遍历获取所有子节点
l=soup.body.children
print(l)     #它返回的是一个listiterator 对象
for i in l:		#既然是个列表迭代器，那肯定能用for循环来偏离取元素
	print(i)

#所有子孙节点  
	#.descendants
for i in soup.descendants:  #.descendants 属性可以对所有tag的子孙节点进行递归循环和
	print(i)				# children类似，我们也需要遍历获取其中的内容

#节点内容 
	#如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
	#如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
print(soup.head.string)
print(soup.title.string)

	#如果 tag 包含了多个子节点,tag 就无法确定string应该调用哪个子节点的内容,输出结果是 None
print(soup.html.string)

#多个内容
	#.strings 获取多个内容，不过需要遍历获取
for i in soup.strings:
	print(i)  

for i in soup.stripped_strings:	#输出的字符串中包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
	print(i)

#父节点 
p=soup.p
print(p.parent.name)

p1 = soup.head.title.string
print(p1.parent.name)

#全部父节点
p2 = soup.head.title.string
for i in p2.parents:
	print(i.name)

#兄弟节点   (关于这个我还没理解透，不知道兄弟节点到底指整个html还是只指同意父节点下的)
	'''
	兄弟节点可以理解为和本节点处在同一级的节点，.next_sibling 属性获取了该节点的下一个兄弟节点，
	.previous_sibling 则与之相反，如果节点不存在，则返回 None
	注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
	因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
	'''
print(soup.p.next_sibling)    #实际输出为空
print(soup.p.previous_sibling) #实际输出为None


#全部兄弟节点  .next_siblings  .previous_siblings 加个s而已，别的一样，不举例

#前后节点   .next_element    .previous_element  
#与 .next_sibling .previous_sibling 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次


#所有前后节点  .next_elements .previous_elements 
#通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样

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


下班，歇了