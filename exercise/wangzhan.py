import requests #导入requests 模块

from bs4 import BeautifulSoup  #导入BeautifulSoup 模块

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器'
web_url = 'http://reeoo.com/'
r = requests.get(web_url, headers=headers) #像目标url地址发送get请求，返回一个response对象
# print(r.text)
# r=requests.get(web_url)
all =BeautifulSoup(r.text)
# print(all.prettify())

all_img =BeautifulSoup(r.text ,"lxml").find_all('a' ,class_='img-part')
all_li =BeautifulSoup(r.text ,"lxml").find_all('li' ,class_='fl')

for li  in all_li:
    print(li['a'])
# print(all_img.__sizeof__())
# for a in all_img:
#     print(a.string)

  # print(a['style'])
  # print(a['img'])
  # print(a['src'])

#
# for img in all_img:
#     print(img['src'])
