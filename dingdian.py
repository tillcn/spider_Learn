#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Connection':'keep-alive'
    }
bash_url = 'http://www.x23us.com/class/'
bashurl = '.html'
for i in range(2,11):
    url_num = bash_url + str(i) + '_1' + bashurl
    head['Referer'] = url_num
    html = requests.get(url_num,headers = head)
    html_doc = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
    soup_sub_max = BeautifulSoup(html_doc, 'lxml').find('em', id="pagestats").get_text()[2:]   #拿到分类的总页数
    for page_num in range(1,int(soup_sub_max) + 1):
        url = bash_url + str(i) + '_' + str(page_num) + bashurl
        html = requests.get(url,headers = head)
        head['Referer'] = url
        html_doc = html.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(html.text)[0])
        soup = BeautifulSoup(html_doc, 'lxml').find_all('tr',{'bgcolor':'#FFFFFF'})
        for k in soup:
            name_soup = k.find('td',class_="L").get_text()[4:]      #拿到书名
            url_soup = k.find('td',class_="L").find('a',target='_blank')['href']    #书的链接
            author_name = k.find('td',class_="C").get_text()        #作者名
            status = k.find_all('td',class_="C")[2].get_text()      #状态，目前是连载还是完结

            chapter_html_iso = requests.get(url_soup, headers = head)
            chapter_html = chapter_html_iso.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(chapter_html_iso.text)[0])
            chapter_soup = BeautifulSoup(chapter_html, 'lxml').find_all('td',class_='L')
            for l in chapter_soup:
                chapter_all = l.find_all('a')
                for chapter in chapter_all:
                    chapter_name = chapter.get_text()
                    text_url = url_soup + chapter['href']
                    head['Referer'] = text_url

                    text_html_iso = requests.get(text_url, headers = head)
                    text_html = text_html_iso.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(text_html_iso.text)[0])         
                    text_soup = BeautifulSoup(text_html, 'lxml').find('dd', id='contents') #正文
                    text_name = BeautifulSoup(text_html, 'lxml').find('div', id='amain').find('dd').find('h1').get_text() #章节名
                    text_txt = str(text_soup).replace('<br/><br/>','\n')
                    text_bsoup = BeautifulSoup(text_txt, 'lxml').get_text().replace('&nbsp','\t')
                    print('正在保存',name_soup,text_name)
                    with open(name_soup+'.txt' ,'a') as f:
                        f.write('\n' + text_name + '\n' + text_bsoup + '\n')
                    time.sleep(10)