import requests

from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=64997'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs = {'class':'title'})


#평점 구하기
total_rates = 0  #전체 평점
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons :
    rate = cartoon.find('strong').get_text()
    print(rate)
    total_rates += float(rate)  #실수형 형태로  tatal_rates에 삽입

print('전체 평점 : ', total_rates)
print('평균 평점 :', total_rates / len(cartoons))


#9.62
#9.69
#9.75
#9.65
#9.58
#9.59
#9.48
#9.51
#9.28
#9.01
#전체 평점 :  95.16000000000001
#평균 평점 : 9.516000000000002
