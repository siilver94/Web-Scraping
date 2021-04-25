from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')         # 웹 드라이버는 Chrome 사용
browser.get('http://naver.com')                          # 네이버 창 열기

elem = browser.find_element_by_class_name('link_login')  # elem 을 로그인 으로 지정

elem.click()          # 로그인 클릭
browser.back()        # 이전 페이지로 이동
browser.refresh()     # 페이지 새로고침
browser.forward()     # 앞 페이지로 이동

elem = browser.find_element_by_id('query')        # elem을 검색창 으로 지정
elem.click()                                      # 클릭

from selenium.webdriver.common.keys import Keys   # 키를 입력 하기 위한 라이브러리 참조

elem.sernd_keys('입력 하고 싶은 문자열')           # 입력 하고 싶은 문자열입력
elem.send_keys(Keys.ENTER)                        # ENTER 키 입력
