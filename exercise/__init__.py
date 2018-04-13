import bs4
import  requests
print("helllosfsdfsf")
a  =requests.get("http://www.baidu.com")
print(a.text)


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup2 = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象

print(soup2.prettify())  # 标准的缩进格式输出
find = soup2.find('p')  #使用find方法查到第一个p标签
print("find's return type is ", type(find))  #输出返回值类型
print("find's content is", find)  #输出find获取的值
print("find's Tag Name is ", find.name)  #输出标签的名字
print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值
print(" navigablestring  is  " , find.string)  #只获取标签的值 ；



markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup  = BeautifulSoup(markup,"lxml")
comment  = soup.b.string
type(comment)
if type(comment)==bs4.element.Comment:
    print("该字符是注释")
else:
    print("该字符不是注释")


soup.head #查找head 标签；
soup.p  # 查找一个p标签 ；

for child  in soup2.children:
    print(child)
for parent in soup2.find('p').parent:
    print(parent)