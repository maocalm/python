import urllib3
import urllib.request
def download():
    # response1 = urllib.request.urlopen('http://httpbin.org/robots.txt')
    # print(response1)
    http=urllib3.PoolManager()
    response=http.request('GET' ,'http://httpbin.org/robots.txt')
    print(response.data)
    print(response.status)
def downloadRet(num):
    try:
        print('pppp')
        html = urllib3.PoolManager().request('GET' ,'http://httpstat.us/500')
        print(html.data)
    except urllib3.exceptions as e :
        print("download erron", e)
        if num >0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return  downloadRet(num-1)
# download()
downloadRet(2)

