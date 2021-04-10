## User Agent

<br/>

**사용자 에이전트(user agent)** 는 사용자를 대표하는 컴퓨터 프로그램으로, 웹 맥락에선 브라우저를 의미합니다.

브라우저 외에도 웹 페이지를 긁어가는 봇, 다운로드 관리자, 웹에 접근하는 다른앱도 사용자 에이전트입니다.

브라우저는 서버에 보내는 모든 요청에 사용자 에이전트 문자열이라고 부르는, 자신의 정체를 알리는 User-Agent (en-US) HTTP 헤더를 보냅니다. 

이 문자열은 보통 브라우저 종류, 버전 번호, 호스트 운영체제를 포함합니다.

스팸 봇, 다운로드 관리자, 일부 브라우저는 자신의 정체를 숨기고 다른 클라이언트인 척 하려고 가짜 사용자 에이전트 문자열을 보내곤 하며, 이를 사용자 에이전트 **스푸핑(spoofing)** 이라고 말합니다.

클라이언트에서는 **JavaScript** 의 **navigator.userAgent (en-US)** 속성을 통해 사용자 에이전트 문자열에 접근할 수 있습니다.

웹 스크래핑을 하기 위해서는자신의 정체를 알리는 `[User-Agent](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/User-Agent)` [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP) 헤더를 보내야 웹스크래핑을 위한 웹 사이트에 접근 할 수 있습니다.

<br/>

### user agent 확인 방법

익스프롤러 마다 다름.

https://www.whatismybrowser.com/detect/what-is-my-user-agent
