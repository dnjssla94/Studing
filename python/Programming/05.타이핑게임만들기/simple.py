import time
import random
import os

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
    user_input = str(input(q+'\n').strip())#앞뒤의 space 제거
    end_time = time.time() - start_time

    if user_input == 'exit':
        break

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]:
            correct += 1

    tot_len = len(q)
    c = correct / tot_len*100
    e = (tot_len-correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f}타/분".format(speed))
    print("정확도 {:0.2f}%".format(c))
    print("오타율 {:0.2f}%".format(e))
    os.system('pause')
    
