# 네이버 웹툰 홈페이지에서 인기순위 1 - 10위까지
# 웹툰 회차 정보 출력
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

print(soup.find('li', attrs={'class': 'rank01'}))

rank1 = soup.find('li', attrs={'class': 'rank01'})
print(rank1.a.get_text())
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling)

rank2 = rank1.next_sibling.next_sibling  # rank1 의 다음 값

rank3 = rank2.next_sibling.next_sibling  # rank2 의 다음 값

print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling  # rank3 의 이전
print(rank2.a.get_text())

print(rank1.parent)  # 부모 값 찾아서 전부 출력

rank2 = rank1.find_next_sibling('li')  # find 함수를 사용하여 li 요소를 간편히 부를 수 있다
print(rank2.a.get_text())

# find 함수를 사용하고 siblings 를 사용하면 형제 원소를 모두 호출 가능.
print(rank1.find_next_siblings('li'))
