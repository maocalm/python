import  urllib.request
import  urllib.error
## 设置代理；
def download (url , user_agent ='wswp' , num_retries=2):
    print('downloading: ' ,url)
    headers =  {'User-agent' : user_agent}
    request = urllib.request.Request(url, headers =headers)  # Request;

    try :
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e :
        print( 'download erro : ' , e.reason )

        html = None
        if num_retries >0 :
            if hasattr( e , 'code') and 500 <= e.code <600 :
                return  download( url , user_agent , num_retries-1)

    return html
