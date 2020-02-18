'''
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자리수만큼 연속 숫자를 포함하는 번호를 생성하는 기능
'''

import numpy #계산관련 라이브러리

def make_lotto_number(**kargs):
    rand_number = numpy.random.choice(range(1,46),6,replace=False) #전시간 짠게 한줄로 numpy 짱 좋다
    rand_number.sort()

    #최종 로또 번호가 완성될 변수
    lotto = []

    if kargs.get("include"):
        include = kargs.get("include")
        lotto.extend(include) #만약 append를 쓰면 list안에 list가 들어갈것.

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make):#for문에서 변수를 직접 쓰지 않을때 _로처리해도됨
            for j in rand_number:
                if lotto.count(j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)

    if kargs.get("exclude"):
        exclude = kargs.get("exclude")
        lotto = list(set(lotto) - set(exclude))

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1,46),6,replace=False) #전시간 짠게 한줄로 numpy 짱 좋다
                rand_number.sort()
                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break

    if kargs.get("continuty"):
        continuty = kargs.get("continuty")
        start_number = numpy.random.choice(lotto,1)#로또 리스트중에서 하나 고름]

        seq_num = []

        for i in range(start_number[0],start_number[0]+continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []

        lotto.extend(seq_num)
        #------------------------------------------
        while len(lotto) != 6:
            for _ in range(cnt_make):
                rand_number = numpy.random.choice(range(1,46),6,replace=False) #전시간 짠게 한줄로 numpy 짱 좋다
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0:
                        lotto.append(j)
                        break

        #-------------------------------------------

    lotto.sort()
    return lotto


result = make_lotto_number(continuty = 2)
print(result)
