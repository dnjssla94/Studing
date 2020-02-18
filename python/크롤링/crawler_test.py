'''
크롤링 순서
1. 원하는 웹페이지에 접속하여 HTML 데이터를 받아온다.
2. 받아온 HTML 데이터를 분석가능한 형태로 가공한다.
3. 원하는 데이터를 가져온다.

sock.py에 구현해봤지만 거기에 HTML데이터를 받아와야하는데 일일이 다 구현할수는 없다.
파이썬 라이브러리를 사용하자
이미 공식화되어있고 라이브러리가 많이있다.
파이썬 내장 라이브러리도 있지만 더 성능이 좋은 requests를 사용하자.
분석 라이브러리는 BeautifulSoup4
'''
import requests
from bs4 import BeautifulSoup   #pip install BeautifulSoup4
from requests_html import HTMLSession # pip install requests_html

response = requests.get("https://www.naver.com")

# print(response.status_code)#200OK
# print(response.headers)#헤더파일
#print(response.text)#html데이터. response.content로도 받을 수 있는데 바이너리, raw데이터 그대로 받아온다.

# bs = BeautifulSoup(response.text,"html.parser") #html.parser은 파이썬 기본 내장.
# #string에서 특정 string을 추출해 내는걸 parsing이라고 한다.
# #print(bs.select("img"))->리스트 형태로 img파일이 추출됨. 보기 편하게 for쓰자
# for i in bs.select("img"):
#     print(i)
#     print("\n")

session = HTMLSession()
response = session.get("https://www.naver.com")
print(response.html.links)