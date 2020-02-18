import time
import random
import os

'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032
예:
chr(((0*21)+0)*28 +0+44032) == '가'
chr(((0*21)+0)*28 +1+44032) == '각'
chr(((1*21)+0)*28 +1+44032) == '깍'
chr(((2*21)+0)*28 +1+44032) == '낙'

초성의 인덱스 = ((x - 44032)/28)/21
중성의 인덱스 = ((x - 44032)/28)%21
종성의 인덱스 = (x - 44032)%28
'''

CHO = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ',
        'ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNG = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ',
        'ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONG = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ',
        'ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ',  
        'ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']



def break_korean(string):
    word_list = list(string)
    break_word = []
    for k in word_list:
        if ord(k) >= ord('가') and ord(k) <= ord('힣'):
            #유니코드상 몇번째 글자인지 인덱스를 구합니다.
            char_index = ord(k) - ord('가')

            # 초성 = (유니코드인덱스 / 28) / 21
            char1 = int((char_index/28)/21)
            break_word.append(CHO[char1])
            #중성 = (유니코드인덱스 / 28) % 21
            char2 = int((char_index/28)%21)
            break_word.append(JUNG[char2])
            #종성 = 유니코드인덱스%28
            char3 = int(char_index%28)
            if char3 > 0:
                break_word.append(JONG[char3])

        else:
            break_word.append(k)

    return break_word

# test = str(input("입력: "))
# result = break_korean(test)
# print("분해: {}".format(result))
Word_list = [
    '네가 없이 웃을 수 있을까 생각만 해도 눈물이나',
    '힘든 시간 날 지켜준 사람 이제는 내가 그댈 지킬 테니',
    '너의 품은 항상 따뜻했어 고단했던 나의 하루에 유일한 휴식처',
    '나는 너 하나로 충분해 긴 말 안 해도 눈빛으로 다 아니깐',
    '한 송이의 꽃이 피고 지는 모든 날, 모든 순간 함께해'
    ]

random.shuffle(Word_list)

for q in Word_list:
    os.system('cls')
    start_time = time.time()
    user_input = str(input(q+'\n')).strip()#앞뒤의 space 제거
    end_time = time.time() - start_time

    src = break_korean(q)
    print(src)
    tar = break_korean(user_input)
    print(tar)

    if user_input == 'exit':
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1

    tot_len = len(src)
    c = correct / tot_len*100
    e = (tot_len-correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f}타/분".format(speed))
    print("정확도 {:0.2f}%".format(c))
    print("오타율 {:0.2f}%".format(e))
    os.system('pause')
    