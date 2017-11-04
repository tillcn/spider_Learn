#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests,os
from bs4 import BeautifulSoup
import os

class BiZhi(object):
    def request(self,all_url):
        headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Connection':'keep-alive',
        'Referer':'https://wall.alphacoders.com/by_resolution.php?w=1920&h=1080&lang=Chinese'
        }
        contnet = requests.get(all_url, headers = headers)
        return contnet

    def all_pages(self,all_url):
        for url_num in range(2,4966):
            page_all= all_url + str(url_num)
            url = self.request(page_all)
            soup = BeautifulSoup(url.text, 'lxml').find('div',id="container_page").find_all('div', class_="thumb-container-big ")
            self.home_url = 'https://wall.alphacoders.com/'
            self.mkdir(url_num)
            os.chdir('d:\\bizhi\\'+'第'+str(url_num)+'页')
            self.sub_page(soup)
            
    def sub_page(self,soup):
        for i in soup:
            k = i.find('a')
            bizhi_name = k['title']
            bizhi_url = self.home_url + k['href']
            down_html = self.request(bizhi_url)
            down_soup = BeautifulSoup(down_html.text, 'lxml').find('img', class_="img-responsive")
            self.photo_name = down_soup['alt']
            self.photo_url = down_soup['src']
            self.save(self.photo_url)

    def save(self,photo_url):
        img = self.request(photo_url)
        m = photo_url[-4:]
        try:
            print('正在保存'+self.photo_name)
            with open(self.photo_name + m, 'ab') as f:
                f.write(img.content)
        except:
            print('这张图片因为错误没有保存')

    def mkdir(self,url_num):
        isexists = os.path.exists(os.path.join('d:\\bizhi','第'+str(url_num)+'页'))
        if not isexists:
            print('创建目录d:\\bizhi\\'+'第'+str(url_num)+'页')
            os.makedirs(os.path.join('d:\\bizhi','第'+str(url_num)+'页'))
            return True
        else:
            print('d:\\bizhi\\ '+'第'+str(url_num)+'页'+'\t目录已存在')
            return False

bizhi = BiZhi()
bizhi.all_pages('https://wall.alphacoders.com/by_resolution.php?w=1920&h=1080&lang=Chinese&page=')
