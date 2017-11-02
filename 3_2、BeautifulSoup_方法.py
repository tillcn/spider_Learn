#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#CSS选择器
    #在写CSS时标签名不加任何修饰，类名前加点,id名前加#
    #也可以利用方法来筛选元素，方法是soup.select() 返回的是列表
soup.select()

#通过标签名查找
soup.select('title')

#通过类名查找
soup.select('.sister')

#通过id名查找
soup.select('#link1')

#组合查找 
    #组合查找和写class文件时，标签名、类名、id名进行组合原理一样
    #例如查找p标签中id等link1的内容，二者需要用空格分开
soup.select('p #link1')

#直接子标签查找
soup.select('head > title')

#属性查找
    #查找时还可以加入属性元素，属性需要用[]括起来，属性和标签属于同一节点
    #中间不能加空格，否则无法匹配
    #同样属性仍然可以与上面的方法组合，不在同一节点的空格隔开，同一节点不加空格
soup.select('a[class="sister"]')
soup.select('a[href="http://example.com/slsie"]')

