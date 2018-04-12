# 35,36,37

import  requests
from bs4 import  BeautifulSoup
import operator

def start(url):
    word_list = []
    # aaa 网络获取
    source_code = requests.get(url).text
    # bbb 检索
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll("a",{"class":"index_single_titles"}):
        content = post_text.string
        # ccc 检索完成一次之后, 进行拆解单词split()
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    # ddd 去除杂质符号
    clean_up_list(word_list)

# 去掉杂质符号 !@#$%^&*
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&&*()"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start("www.google.com")
