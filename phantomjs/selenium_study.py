
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

drive = webdriver.Chrome();
drive.get("http://www.pythom.org")
assert "Python" in drive.title
elem = drive.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert  "no results found ." not in drive.page_source
drive.close()
