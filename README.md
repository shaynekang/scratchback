# scratchback

네이버 뉴스와 인스타그램을 크롤링할 수 있는 라이브러리입니다.

## 설치
프롬프트 창에 `pip install scratchback`을 입력하여 설치할 수 있습니다.

## Naver News Crawler
네이버 뉴스에서도 '속보' 카테고리 정보를 가져오는 크롤러입니다.
### 필요 사항

### 사용 방법

## Instagram Crawler
인스타그램 계정 아이디를 입력하면 계정의 업로드된 게시물 정보를 가져오는 크롤러입니다.
### 필요 사항

인스타그램 크롤러를 사용하기 위해서는 selenium이라는 라이브러리가 필요합니다. 프롬프트 창에 `pip install selenium` 명령어를 입력함으로 selenium을 설치할 수 있습니다. 
만약 jupyter notebook에서 설치하기를 원한다면 `!pip install selenium`을 입력하고 실행시키면 설치가 완료됩니다.

또, Chrome 브라우저로 인스타그램에 접근하기 때문에, [다음의 링크](http://chromedriver.chromium.org/downloads) 에서 크롬 버전에 맞는 드라이버를 다운로드 받아야 합니다. 

작업하고 있는 PC의 크롬 버전은 주소창에 <chrome://version/>를 입력할 경우 알 수 있습니다.   
맨 첫 줄에 Chrome : 75.0.3770.90이라고 나와있을 경우 75 버전의 크롬을 사용하고 있는 것입니다.

### 사용 방법

아래와 같이 라이브러리를 불러올 수 있습니다. 
```python
from scratchback import Instagram
crawler = Instagram()
```
crawler 변수 생성 시 `headless` 옵션을 `False`로 지정하면 Chrome 브라우저를 통해 크롤링 진행 상황을 확인할 수 있습니다.
```python
crawler = Instagram(headless=False)
```
`crawl()` 메소드를 사용하면 크롤링을 할 수 있습니다. 이 때, 첫번째 인자에 Chrome 드라이버의 경로를, 두번째 인자로는 크롤링하고자 하는 계정의 아이디를 입력해주어야 합니다.
```python
post_list = crawler.crawl("chromedriver", "dsschoolkr")
```
`posts` 옵션을 지정하면 가져오려고 하는 게시물의 개수를 조정할 수 있습니다. 아래와 같이 `posts`를 2로 지정할 경우, 해당 계정의 제일 최근 게시물 두개의 정보를 반환합니다.
```python
post_list = crawler.crawl("chromedriver", "dsschoolkr", posts=2)
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

아래의 코드를 통해 결과값을 데이터프레임 형식으로 변환하는 것도 가능합니다.
```python
import pandas as pd
data = pd.DataFrame(post_list)
```
