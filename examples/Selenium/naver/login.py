from selenium import webdriver
import time

browser = webdriver.Chrome(
    'C:\\Users\Vector\Desktop\PythonWorkSpace\.vscode\webscraping_basic\chromedriver.exe')

#1.네이버로 이동
browser.get('http://naver.com')

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()


#3. id,pw 입력
browser.find_element_by_id('id').send_keys('siilver94')
browser.find_element_by_id('pw').send_keys('hack2035')

#4.로그인 버튼 클릭
browser.find_element_by_id('log.login').click()
time.sleep(3)

#5. id를 새로 입력
# browser.find_element_by_id('id').clear()
# browser.find_element_by_id('id').send_keys('siilver94')

#6.html 정보 출력
print(browser.page_source)

qrowser.close()  # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
