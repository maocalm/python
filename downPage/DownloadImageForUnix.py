# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import sys
import urllib
import io
import requests
from PIL import Image
import  os
import time

def getPage(keyword, page, n):
    page = page * n

    keyword = urllib.parse.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onepageurl):
    headers = {
        'Connection': 'close',
    }
    try:
        html = requests.get(onepageurl,headers=headers ,allow_redirects=False).text
    except Exception as e:
        # print('getOnepage_url-------'+e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls ,name ):
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            # iofile  = io.BytesIO(pic.content)
            # im =Image.open(iofile)

            # /home/ec2-user/tensorflow-for-poets-2/tf_files/anim/
            dirString = '/home/ec2-user/imagecached/' +name + '/'
            dirConvertString = '/home/ec2-user/tensorflow-for-poets-2/tf_files/anim/'+name +'/'

            string = '/home/ec2-user/imagecached/' +name + '/' + str(time.time()) + '.jpg'
            stringConvert = '/home/ec2-user/tensorflow-for-poets-2/tf_files/anim/'+name +'/' +str(time.time()) +'convert'+ '.jpg'

            if not os.path.exists(dirString):
                os.makedirs(dirString)
            if  not os.path.exists(dirConvertString):
                os.makedirs(dirConvertString)

            with open(string, 'wb') as f:
                try:
                    f.write(pic.content)
                    im = Image.open(string)
                    im.convert("RGB")
                    im.save(stringConvert)
                except Exception as e :
                    if os.path.exists(stringConvert):
                        os.remove(stringConvert)
                    print('写入失败----------' ,str(e))

                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print('all exception---------'+str(e))
            continue

def start( index  ,name ) :

    keyword = index # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin = 21 
    page_number = 40
    image_number = 100
    all_pic_urls = []
    while 1:
        if page_begin > image_number:
            break
        print("第%d次请求数据", [page_begin])
        url = getPage(keyword, page_begin, page_number)
        onepage_urls = get_onepage_urls(url)
        page_begin += 1

        all_pic_urls.extend(onepage_urls)

    down_pic(list(set(all_pic_urls)) , name)


if __name__ == '__main__':
    # 个人自拍 ，证件照 ，动物 ，美食 ，风景，多人合照 ，手机截图
    items = {'个人自拍': 'Personal selfie', '证件照': 'Document photo', '动物': 'animal'
        , '美食': 'Food', '风景': 'landscape', '多人合照': 'Multi-personphoto', '手机截图': 'Phone-screenshot'}

    for item in items:
        start(item , str(items[item]))