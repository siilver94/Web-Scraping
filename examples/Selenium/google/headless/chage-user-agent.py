from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
browser = webdriver.Chrome(
    'C:\\Users\Vector\Desktop\PythonWorkSpace\.vscode\webscraping_basic\chromedriver.exe', options=options)
browser.maximize_window()


url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()
