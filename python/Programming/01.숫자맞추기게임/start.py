import random
import os

number = random.randint(1,99)
chance = 10
count = 0

os.system("cls")#화면을 깔끔하게 하는 도스 명령어
print("1부터 99까지의 숫자를 10번안에 맞춰보세여")
print("숫자만 입력해야 합니다.")

def input_check(casting=int):
    while True:
        try:
            user_input = casting(input("몇일까요?"))
            return user_input
        except:
            continue


while count < chance:
    count += 1

    user_input = input_check()

    if number == user_input:
        break
    elif user_input < number:
        print("{} 보다 큽니다.".format(user_input))
    elif user_input > number:
        print("{} 보다  작아요.".format(user_input))
    else:
        print("아닙니다.")

if user_input == number:
    print("성공! {}이 맞습니다.".format(number))
else:
    print("실패! 정답은 {}입니다.".format(number))