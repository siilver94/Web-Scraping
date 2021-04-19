import requests
from bs4 import BeautifulSoup

#2015년부터 2020년 까지 1-5위 영화 이미지 다운
for year in range(2015,2020):
    url = ('https://search.daum.net/search?w=tot&q={}\
    %EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR').format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all('img', attrs={'class':'thumb_img'})

    for idx, image in enumerate(images) :
        #print(image['src'])
        #src 에 앞에 https: 붙이기
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:' + image_url

        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        #파일은 예)move_2019_1.jpg 형식으로 만들기
        with open('movie_{}_{}.jpg'.format(year,idx+1), 'wb') as f:
            f.write(image_res.content)
        
        # 상위 5개 이미지 까지만 다운로드
        if idx == 4:
            break
