# 25,26,27 Build a Web Crawler.

import requests
from bs4 import BeautifulSoup



def trade_spider(max_page):

    page = 1
    while page <= max_page:
        # aaa 网络获取资源 按页面
        url = 'https://www.bing.com/images/search?q=' + page
        source_code = requests.get(url)  # Response
        plain_text = source_code.text  # str

        # bbb 获取的html资源进行: 筛选, 排列等处理
        soup = BeautifulSoup(plain_text)  # 可处理的str
        # 'a'html标签名, 表示所有连接. 'class'表示筛选的内容
        for link in soup.find_all('a', {'class': 'item-name'}):
            href = "www.xxx.com" + link.get('href')
            title = link.string
            print(href)
            print(title)

        # aaa 页面+1
        page += 1
trade_spider(1)

def get_item_data(item_url):
    # aaa 网络获取资源 按页面
    source_code = requests.get(item_url)  # Response
    plain_text = source_code.text  # str
    # bbb 获取的html资源进行: 筛选, 排列等处理
    soup = BeautifulSoup(plain_text)  # 可处理的str
    # 'a'html标签名, 表示所有连接. 'class'表示筛选的内容
    for item_name in soup.find_all('div', {'class': 'i-name'}): #findAll
        title = item_name.string
        print(title)
    for link in soup.find_all('a', {'class': 'item-name'}):
        href = "www.xxx.com" + link.get('href')
        print(href)

get_item_data('some_url')

