# web-scraping

<br/>

## 웹 스크래핑 (web scraping)

<br/>


 웹 사이트 상에서 **원하고 필요한 부분**에 위치한 정보를 컴퓨터로 하여금 자동으로 추출하여 수집하는 기술.
 
 <br/>
 
## 웹 크롤링 (web crawling)

<br/>

 **자동화 봇인 웹 크롤러**가 정해진 규칙에 따라 **복수 개의 웹 페이즈**를 브라우징 하는 행위.

> 웹 스크랩 (웹 수집이라고도 함)은 웹 사이트에서 데이터를 추출하는 프로세스입니다. 웹 스크래핑의 목적은 웹에서 공개 되어 있는 데이터를
**자동으로 수집**하여 데이터를 추출하고 저장 한 후 여러가지 용도로 사용하기 위함 입니다.

<br/>

### **봇은 어떻게 콘텐츠를 읽어갈 수 있을까요?**

웹 사이트 스크레이퍼 봇은 일반적으로 일련의 HTTP GET 요청을 보낸 다음 웹 서버가 전송하는 모든 정보를 복사하여 저장하여 웹 사이트가 모든 콘텐츠를 복사 할 수 있습니다.
예를 들어,보다 정교한 스크레이퍼 봇은 JavaScript를 사용하여 웹 사이트의 모든 양식을 작성하고 모든 게이트 된 컨텐츠를 다운로드 할 수 있습니다.
“브라우저 자동화”프로그램 및 API를 사용하면 웹 사이트 및 API가 마치 웹 사용자가 컨텐츠에 액세스한다고 생각하도록 
웹 사이트의 서버를 속이려고 하는 것처럼 웹 사이트 및 API와 자동화 된 봇 상호 작용이 가능합니다.

<br/>

---

## 웹 이란?

<br/>

웹은 크게 **HTML, CSS, JS** 로 있습니다. 

집으로 예를 들자면,

1. 집의 뼈대 역할. (뼈대)  : ***HTML (Hyper Text Markup Language)***
2. 집의 인테리어 역할. (예쁘게하는것)  : ***CSS***
3. 집에서 사람의 역할. (살아있게) :  ***JS***

**VS code** 에서 *'open in browser'* install.

![20210312_203621](https://user-images.githubusercontent.com/57824945/113467804-67046c80-9480-11eb-81f2-206106cad265.png)


설치 후 open in default browser (alt + b) 를 누르면 컴퓨터 설정 기본 브라우져 창 열림

기본적인 html 코드.

<br/>

```html
<html>
    <head>
        <mete charset="utf-8">
        <title>생생이 홈페이지</title>
    </head>
    <body>
        <!-- tpye text는 text, password 는 암호화 되어 나옴 -->
        <input type = "text" value = "아이디를 입력하세요"> 
        <input type = "password">
        <input type = "button" value = "로그인">
        <a href = "http://google.com">구글로 이동하기</a>
    </body>
</html>
```

  ![Untitled](https://user-images.githubusercontent.com/57824945/113468249-84d1d180-9480-11eb-8bdf-91989b829d3b.png)


웹 HTML 을 공부하고 싶다면 해당 사이트 참고.

[W3Schools Online Web Tutorials](https://www.w3schools.com/)
