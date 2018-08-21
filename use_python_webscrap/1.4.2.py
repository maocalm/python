
import re
from  coo import download
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url).decode('utf-8')   #转换为utf
    #print(sitemap)
    #>Downloading: http://example.webscraping.com/sitemap.xml
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print(links)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...

crawl_sitemap('http://example.webscraping.com/sitemap.xml')