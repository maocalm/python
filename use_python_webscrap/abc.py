
import re
import coo
def crawl_sitemap(url):

    # download the sitemap file
    sitemap = download(url)
#>Downloading: http://example.webscraping.com/sitemap.xml
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...

crawl_sitemap('http://example.webscraping.com/sitemap.xml')