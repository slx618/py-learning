# -*- coding=utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import pdfkit
import os
import time
from datetime import datetime as dt
import math


html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
</head>
<body>
{content}
</body>
</html>"""

# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding:gzip, deflate, br
# Accept-Language:zh-CN,zh;q=0.9
# Cache-Control:no-cache
# Connection:keep-alive
# Cookie:Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1513393435,1514267929,1515119311; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1515576335
# Host:www.liaoxuefeng.com
# Pragma:no-cache
# Referer:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432170876125c96f6cc10717484baea0c6da9bee2be4000
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36


def get_url(headers):
    url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'

    headers['Cookie'] = headers['Cookie'] + str(math.ceil(dt.now().timestamp()))
    response = requests.get(url, data=None, headers=headers)
    soup = BeautifulSoup(response.content, "html5lib")

    menu = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for div in menu.find_all("div"):
        url = []

        str_title = str.replace(div.a.string, '/', " & ")
        url.append(str_title)
        url.append("https://www.liaoxuefeng.com" + div.a.get("href"))

        if 'style' in div.attrs:
            if div.attrs['depth'] == '0':
                url.append(1)
            elif div.attrs['depth'] == '1':
                url.append(2)
            elif div.attrs['depth'] == '2':
                url.append(3)
            elif div.attrs['depth'] == '3':
                url.append(4)

        urls.append(url)
    print(urls)
    return urls


def write_html_file(urls, headers):

    key = '1'
    sub_key = '1'
    sub_sub_key = '1'
    for url in urls:
        # 最外层
        if url[2] == 1:
            order = '#'
        # 第一级
        elif url[2] == 2:
            order = key + '.'

            key = str_plus(key)

            sub_key = '1'
            sub_sub_key = '1'
        # 第二级
        elif url[2] == 3:
            order = key + '.' + sub_key
            sub_key = str_plus(sub_key)

            sub_sub_key = '1'
        elif url[2] == 4:
            order =  key + '.' + sub_key + '.' + sub_sub_key
            #sub_key = str_plus(sub_key)
            sub_sub_key = str_plus(sub_sub_key)

        time.sleep(1)
        headers['Cookie'] = headers['Cookie'] + str(math.ceil(dt.now().timestamp()))
        response = requests.get(url[1], data=None, headers=headers)
        soup = BeautifulSoup(response.content, "html5lib")
        body = soup.find_all(class_="x-main-content")[0]

        html = str(body)

        html = complete_real_img(html)

        html = '<h2>' + order + ' ' + url[0] + '</h2>' + html
        html = html_template.format(content=html)
        html = html.encode(encoding="utf-8")

        with open('html/' + order + ' ' + url[0] + '.html', 'wb') as f:
            f.write(html)


def make_html_to_pdf():
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "utf-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

    path = 'html'
    file_list = os.listdir(path)

    file_list = sort_file_name(file_list)

    file_list = [path + '/' + file_name for file_name in file_list]

    file_name = 'app.pdf'
    pdfkit.from_file(file_list, file_name, options=options)


def complete_img_tag(content):
    preg = "<img alt=\"(.*?)\" src=\"(.*?)\"/>"

    images = re.findall(preg, content)

    for path in images:
        content = re.sub(path[1], 'https://www.liaoxuefeng.com' + path[1], content)

    return content


def complete_real_img(content):
    preg = "<img alt=\"(.*?)\" data-src=\"(.*?)\" src=\"(.*?)\"/>"

    images = re.findall(preg, content)

    for path in images:
        content = content.replace(path[2], path[1], 1)

    return content


def str_plus(num):
    num = int(num)
    num += 1
    return str(num)


def sort_file_name(list):

    for index in range(len(list)):
        list[index] = list[index].split('.', 1)

        if(index != 0):
            list[index][0] = int(list[index][0])

    list_first = list[0]
    list = list[1:]

    list.sort()
    list = [list_first] + list

    for index in range(len(list)):
        list[index] = str(list[index][0]) + '.' + list[index][1]
    return list



headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1513393435,1514267929,1515119311,1515640379; atsp=1515654829526_1515654885315; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=',
    'Host':'www.liaoxuefeng.com',
    'Pragma':'no-cache',
    'Referer':'https://www.liaoxuefeng.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# url_list = get_url(headers)
# write_html_file(url_list, headers)
make_html_to_pdf()