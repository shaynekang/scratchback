# scratchback

네이버 뉴스와 인스타그램을 크롤링할 수 있는 라이브러리입니다.

## 필요 사항
최신 버전의 Anaconda를 사용하고 계시는 것을 추천드립니다.

하지만 requests, beautifulsoup4, selenium 라이브러리가 설치되어 있지 않다면 프롬프트(prompt)에서 `pip install requests`, `pip install beautifulsoup4`, `pip install selenium`를 실행하여 `requests`, `beautifulsoup4`, `selenium`를 설치하셔야 라이브러리를 사용할 수 있습니다. http://bit.ly/install-for-crawling 을 참고하여 필요 라이브러리들을 설치해주세요.

만약 jupyter notebook에서 설치하기를 원한다면 `!pip install <라이브러리 이름>`을 입력하고 실행시키면 설치가 완료됩니다.

또, Chrome 브라우저로 인스타그램에 접근하기 때문에, [다음의 링크](http://chromedriver.chromium.org/downloads) 에서 크롬 버전에 맞는 드라이버를 다운로드 받아야 합니다. 

작업하고 있는 PC의 크롬 버전은 주소창에 <chrome://version/>를 입력할 경우 알 수 있습니다.   
맨 첫 줄에 Chrome : 75.0.3770.90이라고 나와있을 경우 75 버전의 크롬을 사용하고 있는 것입니다.

## 설치
프롬프트(prompt) 창에 `pip install scratchback`을 입력하여 설치할 수 있습니다.

## NaverNews Crawler
네이버 뉴스에서도 '속보' 카테고리의 뉴스 정보들을 가져오는 크롤러입니다. 가져오는 정보들로는 `기사 제목, 기사 본문, 기사 날짜, 신문사, 기사 id, 기사 url`가 있습니다.

### 사용 방법
라이브러리를 불러오는 코드는 아래와 같습니다.
```python
from scratchback import NaverNews
crawler = NaverNews()
```
위와 같이 `NaverNews()` 생성 시에 아무 것도 지정하지 않을 경우 코드 실행한 당일 네이버 뉴스 속보 카테고리의 첫 페이지 뉴스 정보를 가져옵니다.

```python
crawler = NaverNews(page_num=3, page_start=4)
```
`page_num`과 `page_start`를 지정함으로써 날짜별로 어느 페이지부터 얼마나 가져올지를 정할 수 있습니다. 만약 `page_num`값을 지정하지 않는다면 날짜별로 하나의 페이지만 가져오며, `page_start`를 정하지 않으면 1페이지부터 가져오도록 설정하였습니다. 또한 현재 존재하는 페이지 수 이상의 페이지 수를 입력하면 존재하는 페이지 수 만큼의 정보만 가져옵니다. 

```python
crawler = NaverNews(page_start=4, page_end=10)
```
`page_num` 대신 `page_end`를 사용하여 어디에서부터 어디까지 정보를 가져올지 설정할 수 있습니다. 만약 `page_num`, `page_start`, `page_end`를 셋 다 설정하였는데 `page_num`이 `page_end - page_start + 1`값과 일치하지 않을 경우 에러가 발생하니 유의하시기 바랍니다. `page_start`, `page_end`를 지정할 경우 `page_num`을 지정하지 않아도 됩니다.

```python
crawler = NaverNews(date_start="2019.06.14")
```
변수로 날짜를 지정하여 정보를 가져올 수 있으며 입력하는 날짜의 양식은 YYYY.MM.DD로, 다른 양식은 작동하지 않습니다. 따로 날짜를 지정하지 않으면 오늘 날짜로 지정되고 미래의 날짜를 입력해도 자동으로 오늘의 날짜로 지정됩니다. 날짜를 입력하는 변수는 `date_start`와 `date_end`가 있습니다. 위의 코드의 경우 2019년 6월 14일부터 코드를 실행하는 날까지의 뉴스 속보를 가져오며, 일별로 한 페이지만을 가져오는 기능을 합니다.
```python
crawler = NaverNews(date_start="2019.06.14", date_end="2019.06.16")
```
`date_end` 변수를 통해 가져오고자 하는 날의 마지막도 지정할 수 있습니다. `date_end`를 따로 지정하지 않는 다면 오늘 날짜로 지정됩니다. 

만약 2019년 6월 14일부터 6월 16일까지의 뉴스 속보를 날짜별로 1페이지부터 10페이지까지 가져오고 싶다면, 다음과 같은 코드를 통해 크롤링할 수 있습니다.
```python
crawler = NaverNews(page_start=1, page_end=10, date_start="2019.06.14", date_end="2019.06.16")
```
`crawl()` 메소드를 사용하여 네이버 뉴스 속보 정보를 가져올 수 있습니다.
```python
news_list = crawler.crawl()
```

결과값인 news_list의 형태는 다음과 같습니다.
```python
{'headline': '[날씨] 오늘 초여름 더위 속 곳곳 소나기...제주도 ·남해안 비',
  'content': '오늘도 초여름 더위가 이어지는 가운데 내륙 곳곳에 소나기가, 제주도와 남해안에는 비가 내릴 것으로 보입니다.기상청은 오늘 제주도와 남해안은 남쪽을 지나가는 기압골 영향으로 5~30mm의 비가 오겠다고 밝혔습니다.내륙은 대체로 맑겠지만, 영서와 경북과 전북 내륙에는 대기 불안정으로 오후 한때 소나기가 내리는 곳이 있겠습니다.오늘 낮 기온은 서울과 대전·대구 27도 등 어제보다 1∼2도 낮지만, 여전히 덥겠습니다.[저작권자(c) YTN & YTN PLUS 무단전재 및 재배포 금지]',
  'written at': datetime.date(2019, 6, 14),
  'company': 'YTN',
  'url': 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=052&aid=0001306642',
  'title': '2번째 뉴스',
  'id': '052-0001306642'}
```
리스트 내에 각각의 뉴스에 대한 정보가 딕셔너리 형태로 들어있는 모습입니다.

아래의 코드를 통해 결과값을 데이터프레임 형식으로 변환한 뒤 csv파일로 저장할 수 있습니다.
```python
import pandas as pd
data = pd.DataFrame(news_list)
data.to_csv("news.csv")
```

## Instagram Crawler
인스타그램 계정 아이디를 입력하면 계정의 업로드된 게시물 정보를 가져오는 크롤러입니다.  
페이지 로딩에 1분 이상 소요될 경우 프로그램이 멈추도록 설계되어 있습니다. 인터넷 환경이 원활한 곳에서 사용하는 것을 권장드립니다.

### 사용 방법

아래와 같이 라이브러리를 불러올 수 있습니다. Instagram 객체 생성 시, 다운로드 받은 chromedriver의 경로를 입력해주어야 합니다.
```python
from scratchback import Instagram
crawler = Instagram("chromedriver")
```
crawler 변수 생성 시 `headless` 옵션을 `False`로 지정하면 Chrome 브라우저를 통해 크롤링 진행 상황을 확인할 수 있습니다.
```python
crawler = Instagram("chromedriver", headless=False)
```
`crawl()` 메소드를 사용하면 크롤링을 할 수 있습니다. 이 때, 크롤링하고자 하는 계정의 아이디를 입력해주어야 합니다.
```python
post_list = crawler.crawl("dsschoolkr")
```
`posts` 옵션을 지정하면 가져오려고 하는 게시물의 개수를 조정할 수 있습니다. 아래와 같이 `posts`를 2로 지정할 경우, 해당 계정의 제일 최근 게시물 두개의 정보를 반환합니다.
```python
post_list = crawler.crawl("dsschoolkr", posts=2)
```
결과값인 `post_list`의 형태는 아래와 같습니다.
```python
[{'comments': '0',
  'content': '오늘밤(6/9) 8시 유튜브 스트리밍으로 스타벅스 1호 데이터사이언티스트가 직업/전망/데이터와 관련된 질문에 직접 답변드립니다 :)참여방법은 프로필 설명을 확인해주세요!',
  'img_src': ['https://scontent-icn1-1.cdninstagram.com/vp/0665d8f0404e266aa84d3d77eb919b56/5DC64220/t51.2885-15/e35/61234597_166094021086395_2911502642251464796_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com'],
  'like': '8',
  'post_id': 'ByezZRLBSjV'}]
```
리스트 내에 각각의 게시물에 대한 정보가 딕셔너리 형태로 들어있는 모습입니다.

`post_id`는 게시물의 고유 id를 의미합니다. `img_src`에는 이미지 혹은 동영상의 url 정보가 리스트 형태로 담겨있으며, `content`에는 게시물에 작성된 문구가 담겨있습니다. `like`는 게시물 좋아요 개수, `comments`는 게시물에 달린 댓글의 개수를 의미합니다.

아래의 코드를 통해 결과값을 데이터프레임 형식으로 변환하고 csv파일로 저장할 수 있습니다.
```python
import pandas as pd
data = pd.DataFrame(post_list)
data.to_csv("post.csv")
```
