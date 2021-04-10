# 라이브러리 설치.

<br/>

콘솔 창에 **Web Scraping** 에 필요한 라이브러리 pip 명령으로 다운.

<br/>

## xml (Extensible Markup Language)

**XML**이란 단순한 문자열을 넘어서서, 내부적으로 트리 구조를 가지고 있는 파일을 표현하기 위해 사용하는 마크업 언어입니다.

웹페이지를 보여주기 위해 사용되는 **html** 파일이 **XML**의 가장 대표적인 예시입니다. 

그뿐만이 아니라 우리가 친숙하게 사용하는 **MS Office**의 **워드, 엑셀, 파워포인트** 파일 **(docx, xlsx, pptx)** 도 **XML** 의 일종입니다.

따라서 **XML**을 해석하는 프로그램(**parser**)을 미리 준비해야 **html, docx, xlsx, pptx**와 같이 우리가 흔히 다루는 파일을 처리할 수 있습니다. 
**Python**에서 **XML parser**로서 주로 이용되는 패키지는 **lxml**입니다. 


`pip install lxml`

<br/>

## beautifulsoup4

<br/>

**BeautifulSoup**는 우리의 크롤링을 도와줄 파이썬 오픈소스 라이브러리 입니다.

정규표현식을 사용해서 **크롤링**한 데이터 **(html, xml등)** 내에서 원하는 부분을 추출할 수 있도록 도와줍니다.

`pip install beautifulsoup4`
