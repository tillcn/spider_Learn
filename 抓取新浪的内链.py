#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(page_url):
    global pages
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Connection':'keep-alive'
    }
    html = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    for url in soup.find_all('a', href = re.compile(r'(sina.com/)')):
        if 'href' in url.attrs:
            if url.attrs['href'] not in pages:
                print('发现新链接')
                new_url = url.attrs['href']
                name = url.string
                pages.add(new_url)
                with open('sina_links.txt', 'a+') as f:
                    f.write(str(pages)+'\n\n')
                getlinks(new_url)

getlinks('http://www.sina.com')




