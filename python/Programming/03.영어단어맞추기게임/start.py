import random

words_dict = {
    " 사자" : "lion",
    "호랑이" : "tiger",
    "사과" : "apple",
    "비행기" : "airplane",
    "잔" : "cup"
}

words = []

for word in  words_dict:
    words.append(word)

random.shuffle(word)

chance = 3

for i in range(0, len(words)):
    q = words[i]
    for j in range(0,chance):
        user_input = str(input("{}의 영어단어를 입력하시오: ".format(q)))
        english = words_dict[q]

        if user_input.lower().strip() == english.lower(): #소문자, 공백제거 하고 비교
            print("정답!")
            break
        else:
            print("틀렸습니다!")
    if user_input != english:
        print("정답은 {} 입니다.".format(english))

print("모든 문제를 다 풀었습니다.")