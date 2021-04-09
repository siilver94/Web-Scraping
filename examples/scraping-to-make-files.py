#Google 사이트를 mygoogle.html 이름을 가진 파일로 생성.

import requests
res = requests.get("http://google.com")
res.raise_for_status()

print('정상입니다')

print(len(res.text))
print(res.text)

with open('mygoogle.html','w',encoding = 'utf8)') as f:
    f.write(res.text)
