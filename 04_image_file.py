# 21 Module. 22 Download Image from web. 23 Read/Write file.
# 24 Download the file from the web.


# Setting >> Project interpreter

# 21 Module.
import m #自定义的
import random #Python自带的
# import urllib.request
from urllib import  request


m.fish()
x = random.randrange(100,1000)
print(x)

# 22 Download Image from web.
def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    request.urlretrieve(url,full_name) #下载后的命名

download_image("http://teachlikeachampion.com/wp-content/uploads/good2.jpg")

# 23 Read/Write file
fw = open("sample.txt", "w") # 1创建, 2写入内容, 3关闭
fw.write("Writing some stuff in my text file\n")
fw.write("I love it")
fw.close()

fr = open("sample.txt","r")
text = fr.read()
print(text)
fr.close()

# 24 Download the file from the web

my_url = 'https://stackoverflow.com/questions/10195915/python-urllib2-httperror-http-error-401-unauthorized'
def download_data(url):
    # aaa 读取网络资源
    response = request.urlopen(url) #response
    file_data = response.read() #data 机器码
    file_str = str(file_data) #string 人的字符
    lines = file_str.split("\\n") #line 字符分行

    #将资源写入本地文件中
    dest_url = r"goog.txt"
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_data(my_url)


# 25 Build a Web Crawler.



