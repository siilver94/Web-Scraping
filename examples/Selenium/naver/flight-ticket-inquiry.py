from selenium import webdriver
import time

#셀레니움 메크로 중, 로딩시간일때 끝나면 다음 항목으로 이동
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    'C:\\Users\Vector\Desktop\PythonWorkSpace\.vscode\webscraping_basic\chromedriver.exe')
browser.maximize_window()  # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url)  # url 로 이동

browser.find_element_by_link_text('가는날 선택').click()

# 다음달 27, 27 선택
browser.find_elements_by_link_text("1")[1].click()  # -> 다음달
browser.find_elements_by_link_text("2")[1].click()  # -> 다음달

# 제주도 선택
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]/div/dl/dt").click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 해당 xpath란 조건으로 엘리먼트가 나올 때 까지 최대 10초간 브라우져를 대기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located
        ((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
     # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

elem = browser.find_element_by_xpath(
     "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)

time.sleep(300)
