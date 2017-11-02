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
	os.makedirs(os.path.join('d:\\biqu',name))
	os.chdir('d:\\biqu\\'+name)
	html_b = requests.get(book_url,headers=headers)
	soup_b = BeautifulSoup(html_b.text, 'lxml')
	soup_ba = soup_b.find('div', class_="listmain").find_all('a')
	with open('d:\\biqu\\all.txt', 'a+', encoding='utf-8') as f:
		f.write(name+'\t'+book_url+'\n') 
	for zhangjie in soup_ba:
		zhang_name = zhangjie.string
		zhang_url = home_url + zhangjie['href']
		with open(name+'.txt','a+', encoding='utf-8') as f:
			f.write(zhang_name+'\t'+zhang_url+'\n')

