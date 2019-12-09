from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
import time

def fz(site):
    start = datetime.datetime.now()
    options = webdriver.ChromeOptions()
    #options.headless = True
    browser = webdriver.Chrome(executable_path="C:\\Users\\Farouk\\Desktop\\python projects\\chromedriver.exe", options=options)
    browser.get("https://fzmovies.net")
    search = browser.find_element_by_id("searchname").send_keys(site)
    search_button = browser.find_element_by_name("Search")
    search_button.click()
    time.sleep(2)
    title = browser.find_element_by_xpath("/html/body/div[15]/table/tbody/tr/td[2]/span/a")
    browser.execute_script("arguments[0].click();", title)

    down = browser.find_element_by_id("downloadoptionslink2")
    browser.execute_script("arguments[0].click();", down)
    downlink = browser.find_element_by_id("downloadlink")
    browser.execute_script("arguments[0].click();", downlink)
    jj = browser.find_element_by_name("download1")
    link = jj.get_attribute("value")

    print(link)
    stop = datetime.datetime.now()
    result = stop - start
    print(result, 'seconds')
    browser.quit()
    return link
ss = input("Enter the movie you want to download: ")
print(fz(ss))
input("Press Enter to close.....")
