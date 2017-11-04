#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests,os
from bs4 import BeautifulSoup
import os

def request(all_url):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Connection':'keep-alive',
    'Referer':'https://wall.alphacoders.com/by_resolution.php?w=1920&h=1080&lang=Chinese'
    }
    contnet = requests.get(all_url, headers = headers)
    return contnet
img_num = 0
for url_num in range(2,4966):
    print('一共下载了'+str(img_num)+'页壁纸')
    img_num += 1
    url_all= 'https://wall.alphacoders.com/by_resolution.php?w=1920&h=1080&lang=Chinese&page=' + str(url_num)
    url = request(url_all)
    soup = BeautifulSoup(url.text, 'lxml').find('div',id="container_page").find_all('div', class_="thumb-container-big ")
    home_url = 'https://wall.alphacoders.com/'
    name_url_save = {}
    #url_down = []          本来想记录下载链接然后后面使用的，但不用也挺好，先留着，封装class时再用
    isexists = os.path.exists(os.path.join('d:\\bizhi','第'+str(url_num)+'页')) #.exists方法判断name是否存在，存在返回True
    if not isexists:
        print('创建目录d:\\bizhi\\'+'第'+str(url_num)+'页')
        os.makedirs(os.path.join('d:\\bizhi','第'+str(url_num)+'页'))
    else:
        print('d:\\bizhi\\ '+'第'+str(url_num)+'页'+'目录已存在')
    os.chdir('d:\\bizhi\\'+'第'+str(url_num)+'页')
    num=0
    for i in soup:
        k = i.find('a')
        bizhi_name = k['title']
        bizhi_url = home_url + k['href']
        down_html = request(bizhi_url)
        down_soup = BeautifulSoup(down_html.text, 'lxml').find('img', class_="img-responsive")
        photo_name = down_soup['alt']
        photo_url = down_soup['src']
        name_url_save[photo_name] = photo_url
        url_down.append(photo_url)
        img = request(photo_url)
        m = photo_url[-4:]
        try:
            with open('bizhi.txt', 'a+') as f_dict:
                f_dict.write(photo_name +'\t' + photo_url+'\n')
        except:
            print('这一条信息因为错误没保存')
        try:
            num += 1
            i1 = str(num)
            print('正在保存第'+i1+'张')
            with open(photo_name + m, 'ab') as f:
                f.write(img.content)
        except:
            print('这张图片因为错误没有保存')
