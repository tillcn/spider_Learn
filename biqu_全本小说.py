#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
home_url = 'http://www.biqukan.com'
url_wanben = 'http://www.biqukan.com/wanben'
url = requests.get(url_wanben,headers=headers)
soup = BeautifulSoup(url.text, 'lxml')
soup_a = soup.find('div',class_="up").find('ul').find_all('a')
for i in soup_a[::2]:
	name = i.string
	book_url = home_url + i['href']
	isexists = os.path.exists(os.path.join('d:\\biqu',name)) #.exists方法判断name是否存在，存在返回True
	if not isexists:
		print('创建名为',name,'的目录')
		os.makedirs(os.path.join('d:\\biqu',name))
	else:
		print('名称为',name,'的目录已存在')
	os.chdir('d:\\biqu\\'+name)
	html_b = requests.get(book_url,headers=headers)
	soup_b = BeautifulSoup(html_b.text, 'lxml')
	soup_ba = soup_b.find('div', class_="listmain").find_all('a')
	with open('d:\\biqu\\all.txt', 'w', encoding='utf-8') as f:
		f.write(name+'\t'+book_url+'\n') 
	for zhangjie in soup_ba:
		zhang_name = zhangjie.string
		zhang_url = home_url + zhangjie['href']
		with open(name+'.txt','w', encoding='utf-8') as f:
			f.write(zhang_name+'\t'+zhang_url+'\n')
		html_text = requests.get(zhang_url, headers=headers)
		soup_text = BeautifulSoup(html_text.text, 'lxml')
		soup_zhang = soup_text.find('div', class_="book reader").find('div', class_="showtxt")

		#获取文本有两种写法
		# 下面是第一种
		with open(name+'全文.txt','w', encoding='utf-8') as f:
			f.write(soup_zhang.get_text())

		# 这是第二种,以行为单位来操作，能在行尾加个\n等,排版灵活一点，当然排版还有别的方法
		#但是这种方法需要加条件，不然只能抓取最后一章
		# for text_w in soup_zhang:
		# 	with open(name+'全文.txt','w', encoding='utf-8') as f:
		# 		f.write(str(text_w.string)+'\n')
		


