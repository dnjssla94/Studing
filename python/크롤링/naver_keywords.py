import requests
from bs4 import BeautifulSoup
import time

def time_function(f):
    def wrapper(*args, **kargs):
        start_time = time.time()
        result = f(*args, **kargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper

@time_function
def r_find_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li", {"class": "ah_item"})

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles

@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.select("li.ah_item")

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles

r = requests.get("https://www.naver.com")
#bs = BeautifulSoup(r.text, "html.parser")
bs = BeautifulSoup(r.text, "lxml") #pip install lxml
'''
lxml이 html.parser보다 속도면에서 좀더 좋다.
'''
lists = bs.select("li.ah_item")#select는 이렇게 접근한다. find 함수랑 다르다.
for li in lists:
    title = li.select("span.ah_k")[0].text#select는 항상 list를 리턴. index를 해줘야한다. .text는 find와 같은기능.
    print(title)
'''
select에서 표기법:
클레스의 경우: li.클레스
아이디의 경우: li#아이디   
예:
<li class = a id = b> 일 경우
li.a ->클래스로 접근
li#b ->아이디로 접근
무엇으로 접근할지는 클래스나 아이디가 어디에 사용되고 있는지
개발자 도구를 확인하고, 찍어보고 하면서 결정.
'''

# lists = bs.find_all("li", {"class": "ah_item"})
# for li in lists:
#     #print(li)
#     title = li.find("span",{"class":"ah_k"}).text #.text->태그사이에 위치한 내용만 뽑음
#     print(title)
#     #print('\n')

url = "https://www.naver.com"
r_find_all(url,"html.parser")#제일 느림
r_select(url,"html.parser")

r_find_all(url,"lxml")
r_select(url,"lxml")#제일빠름