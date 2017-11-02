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




