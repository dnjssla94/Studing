import requests
from bs4 import BeautifulSoup
import re
import json
import random
import os

def get_news():
    url = 'https://www.usatoday.com'
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("div.gnt_m_th > a")

    for li in lists:
        href = url+li["href"]#주소는 a 태그의 href
        #print(href)

        r = requests.get(href)
        bs = BeautifulSoup(r.text,"lxml")
        texts = bs.select('div.gnt_ar_b > p.gnt_ar_b_p')
        contents = [p.text for p in texts]
        # contents = []
        # for p in texts:
        #     contents.append(p.text)

        contents = ''.join(contents)
        #print(contents)
        return contents.lower()
    return None

def naver_translate(word):
    try:
        url = 'https://ac.dict.naver.com/enkodict/ac?st=11001&r_lt=11001&q={}'.format(word)
        r = requests.get(url)
        j = json.loads(r.text)
        return j['items'][0][0][1][0]
    except:
        return None

def make_quize(news):
    match_pattern = re.findall(r'\b[a-z]{4,15}\b',news)
    #print(match_pattern)

    quize_list = []
    frequency = {}

    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count +1

    for word, count in frequency.items():
        #print(word, count)
        if count > 1:
            kor = naver_translate(word)
            if kor is not None:
                quize_list.append({kor: word})

    return quize_list


# news = get_news()
# quize = make_quize(news)
#test = naver_translate("man")

def quize():
    quize_list = make_quize(get_news())
    random.shuffle(quize_list)

    chance = 5
    count = 0
    for q in quize_list:
        count += 1
        kor = list(q.keys())[0]
        english = q.get(kor)
        os.system('cls')

        print('*'*60)
        print('문제: {}'.format(kor))
        print('*'*60)

        for j in range(chance):
            user_input = str(input("위의 뜻이 의미하는 단어를 입력하시오: ")).strip().lower()
            print('\n')
            if user_input == english:
                print("정답입니다! {}문제 남음".format(len(quize_list)-count))
                os.system('pause')
                break
            elif j<4:
                print('오답입니다. {}번의 기회가 남았습니다.'.format(chance-j))
                
            else:
                print("정답은 {}입니다. 다음 문제로 넘어갑니다.".format(english))
                os.system('pause')
    print('더이상 문제가 없습니다.')

quize()