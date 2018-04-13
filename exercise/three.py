import  urllib.request
from  bs4  import  BeautifulSoup
url = "http://reeoo.com"
content  =urllib.request.urlopen(url).read();

soup  =  BeautifulSoup(content)
img_all  = soup.find_all('img')
for img  in img_all :
    print(img['src'])