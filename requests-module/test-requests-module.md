 ## 기본 requests 동작
 
 <br/>
 
 `res.raise_for_status()` 는 문제가 생기면 중지하고, 문제가 없으면 없으면 웹 스크래핑 진행한다.

```python
import requests

res = requests.get("http://naver.com")
print('응답코드 :', res.status_code) # 200이면 정상

if res.status_code == requests.codes.ok :
    print('정상입니다')
else:
    print('문제가 생겼습니다. [에러코드 ', res.status_code< "]")
```

 <br/>

위의 코드를 아래와 같이 단 세줄로 간소화가 가능 합니다.

 <br/>

```python
import requests
res = requests.get("http://naver.com")
res.raise_for_status()
```
