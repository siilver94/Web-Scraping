## Headless Chrome

<br/>

서버 같은 곳에서 작업을 할때, 불필요 하게 매번 브라우져를 띄워 결과를 확인하면 불필요한 많은  메모리를 잡아 먹습니다.
크롬이 없는 크롬. 크롬을 띄우지 않고 크롬을 실행시키면 메모리 적으로 매우 효율 적인 작업이 가능합니다.

백그라운드에서 실행 크롬이 없는 크롬을 실행을 시켜서 좀더 빠르게 실행 가능 합니다.

아래 코드를 작성하여 headless 를 True 로 해주면 크롬 창을 띄우지 않고 실행.

```py
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
```

<br/>

