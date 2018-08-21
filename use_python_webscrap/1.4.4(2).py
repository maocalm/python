import  re
import urllib.parse
from  coo import download
import time
import socket
# socket.getaddrinfo('127.0.0.1', 8388)
# print(socket.getaddrinfo('127.0.0.1', 8388))

def link_crawler ( seed_url , link_regex):
    crawl_queue = [seed_url]  #  liebiao ;

    seen = set(crawl_queue)
    while  crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        print(333333333,get_links(str(html)).__sizeof__())
        for link in get_links(str(html)) :
            time.sleep(0.03)
            print('-------------')
            if re.findall(link_regex ,link):
                print('++++++++++++',link)
                link = urllib.parse.urljoin( seed_url , link )
                if  link not in seen  :
                    seen.add(link)
                    crawl_queue.append(link)

    print('size' ,crawl_queue)

def get_links(html):
    # webpage_regex = re.compile('<a[^>] + href=["\'](.*?)["\']' ,re.IGNORECASE)
    print(html)
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


link_crawler('http://example.webscraping.com/places/default' , '/(index|view)')