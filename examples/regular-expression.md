## 정규화 표현식 Regular Expression

<br/>

`p = re.compile('원하는 형태')`

`m = p.match('비교할 문자열') `  :  주어진 문자열의 처음부터 일치하는지 확인.

`m = p.search('비교할 문자열') `  :  주어진 문자열 중에 일차하는게 있는지 확인.

`lst = p.findall('비교할 문자열)`    :  일치하는 모든 것을 리스트 형태로 반환.

<br/>

### 정규식 예  

<br/>

 . : 하나의 문자를 의미.
 
 ^ : 문자열의 시작.
 
 $ : 문자열의 끝.
 

<br/>

```python

#파이썬에서 정규 표현식을 지원하는 re 모듈
import re

p = re.compile('ca.e')

def print_match(m): 
    if m:
        print('m.group() : ', m.group())   # 일치하는 문자열 반환
        print('m.string : ' , m.string)    # 입력받은 문자열
        print('m.start() : ', m.start())   # 일차하는 문자열의 시작 index
        print('m.end() :', m.end())        # 일치하는 문자열의 끝 index
        print('m.span() :', m.span())      # 일치하는 문자열의 시작/끝 index
    else:
        print('매칭 되지 않음')

m = p.search('good care')
print_match(m)

lst = p.findall('good care cafe')   # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)
```

`m.group() : care`

`m.string : good care`

`m.start() : 5`

`m.end() : 9`

`m.span() : (5, 9)`

`['care', 'cafe']`
