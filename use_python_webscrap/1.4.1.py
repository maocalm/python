
import urllib3
import  urllib.request
import  urllib.error

def download1(url):
    """Simple downloader"""
    return urllib.request.urlopen(url).read()

print(download1('https://www.baidu.com'))



print('--------------------')

def download2(url):
    print("downlaoding:" +url)
    try :
        html = urllib.request.urlopen(url).read()
    except urllib.error as e :
        print( 'download erro :' , e.reason )
        html = None
    return  html


print(download2('https://www.baidu.com')) # 必须加http;


#503 服务器过载错误；可以尝试重试下载 ，不过404 就没必重试了； （4 发生在请求的错误 ，5 服务端的错误； ）



print('*---------------3--------------------')
#重试功能的demo;
def download3 (url , num_retries =2 ) :
    print('downloading :' ,url )
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e :   # 指定错误是什么；  
        print( 'download erro :' ,e.reason)
        html = None

        if num_retries >0 :
            if hasattr( e , 'code') and 500 <= e.code <600 :
                #  retry http erros
                return  download3(url ,num_retries-1)
    return  html

download3('http://httpstat.us/500' ,2)   #参数补全；

