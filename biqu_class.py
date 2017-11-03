#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Biqu(object):
    def __init__(self):
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Connection':'keep-alive'
		}
        self.home_url = 'http://www.biqukan.com'

    def request(self,url_home):
        contner = requests.get(url_home, headers = self.headers)
        return contner

    def get_all(self,url_home):
        all_url = self.request(url_home)
        soup_a = BeautifulSoup(all_url.text, 'lxml').find('div',class_='up').find('ul').find_all('a')
        self.book_list = []
        for i in soup_a[::2]:
            self.name = i.string
            book_url = self.home_url + i['href']
            self.mkdir(self.name)
            os.chdir('/soft/biqu/' + self.name)
            with open('/soft/biqu/all.txt', 'a')as all_book:
                all_book.write(self.name + '\t' + book_url +'\n')
                self.get_book(book_url)
        
    def get_book(self, book_url):
        book_html = self.request(book_url)
        self.headers['Referer'] = book_url
        soup_b = BeautifulSoup(book_html.text, 'lxml').find('div', class_='listmain').find_all('a')
        for chapter in soup_b:
            chapter_name = chapter.string
            chapter_url = self.home_url + chapter['href']
            with open(self.name+'.txt', 'a') as book:
                book.write(chapter_name+'\t'+chapter_url+'\n')
                self.get_chapter(chapter_url)

    def get_chapter(self, chapter_url):
        chapter_html = self.request(chapter_url)
        soup_c = BeautifulSoup(chapter_html.text, 'lxml').find('div', class_="book reader").find('div', class_="showtxt")
        with open(self.name+'全文.txt', 'a') as chapter:
            chapter.write(soup_c.get_text())

    def mkdir(self, name):
        isexists = os.path.exists(os.path.join('/soft/biqu', name))
        if not isexists:
            print('创建名为',name,'的目录')
            os.makedirs(os.path.join('/soft/biqu', name))
            return True
        else:
            print('名为',name,'的目录已存在')
            return False
        
biqu = Biqu()
biqu.get_all('http://www.biqukan.com/wanben')