#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Connection':'keep-alive'
    }
bash_url = 'http://www.x23us.com/class/'
bashurl = '.html'
for i in range(1,11):
    url = bash_url + str(i) + '_1' + bashurl
    html = requests.get(url,headers = head)
    html_doc = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    soup = BeautifulSoup(html_doc, 'lxml').find_all('tr',{'bgcolor':'#FFFFFF'})
    for k in soup:
        name_soup = k.find('td',class_="L").get_text()[4:]      #拿到书名
        url_soup = k.find('td',class_="L").find('a')['href']    #书的链接
        author_name = k.find('td',class_="C").get_text()        #作者名
        status = k.find_all('td',class_="C")[2].get_text()      #状态，目前是连载还是完结

        sub_html_iso = requests.get(url_soup, headers = head)
        sub_html = sub_html_iso.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(sub_html_iso.text)[0])
        chapter_url = BeautifulSoup(sub_html, 'lxml').find('a', class_="read")['href'] #进入章节列表链接

        chapter_html_iso = requests.get(chapter_url, headers = head)
        chapter_html = chapter_html_iso.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(chapter_html_iso.text)[0])
        chapter_soup = BeautifulSoup(chapter_html, 'lxml').find_all('td',class_='L')
        for l in chapter_soup:
            chapter_all = l.find_all('a')
            for chapter in chapter_all:
                chapter_name = chapter.get_text()
                text_url = chapter_url + chapter['href']
                print(chapter_name, text_url)



        


