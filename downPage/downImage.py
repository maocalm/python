# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import sys
import urllib
import io
import requests
from PIL import Image
import  os

def getPage(keyword, page, n):
    page = page * n
    keyword = urllib.parse.quote(keyword, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyword + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onepageurl):
    try:
        html = requests.get(onepageurl).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls):
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            # iofile  = io.BytesIO(pic.content)
            # im =Image.open(iofile)

            # /home/ec2-user/tensorflow-for-poets-2/tf_files/anim/
            string = 'C:/Users/hanwenmao/Desktop/bull/one/' + str(i + 1) + '.jpg'
            stringConvert = 'C:/Users/hanwenmao/Desktop/bull/' + str(i + 1) +'convert'+ '.jpg'

            with open(string, 'wb') as f:
                f.write(pic.content)
                im = Image.open(string)
                im.convert("RGB")
                try:
                    im.save(stringConvert)
                except Exception as e :
                    os.remove(stringConvert)

                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue


if __name__ == '__main__':
    # 个人自拍 ，证件照 ，动物 ，美食 ，风景，多人合照 ，手机截图
    items = {'个人自拍':'Personal selfie' ,'证件照':'Document photo' ,'动物':'animal'
        ,'美食':'Food' ,'风景':'landscape','多人合照':'Multi-personphoto' ,'手机截图':'Phone-screenshot'}

    keyword = '动物'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin = 0
    page_number = 80
    image_number = 3
    all_pic_urls = []
    while 1:
        if page_begin > image_number:
            break
        print("第%d次请求数据", [page_begin])
        url = getPage(keyword, page_begin, page_number)
        onepage_urls = get_onepage_urls(url)
        page_begin += 1

        all_pic_urls.extend(onepage_urls)

    down_pic(list(set(all_pic_urls)))
