# 네이버 웹툰 만화중 '나이트런' 의 만화 제목, 링크 가져오기
import requests

from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=64997'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs = {'class':'title'})  #td element 중 title이 클래스 인것

#만화 제목 + 링크 가져오기 
#title 의 text만 추출하고, a element 가 href(링크) 추출하기 
for cartoon in cartoons :
     title = cartoon.a.get_text()
     link = 'https://comic.naver.com' + cartoon.a['href']
     print(title,'\n\n',link)
