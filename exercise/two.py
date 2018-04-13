import  requests
import bs4

web_url  = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=pocket"
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response  = requests.get(web_url,headers = head)
all_img = bs4.BeautifulSoup(response.text, 'lxml').find_all('a')
for img in  all_img:
    print(img)

image=bs4.BeautifulSoup(response.text ,'lxml').select('.lazy')

for img in image :
    print(img.string)