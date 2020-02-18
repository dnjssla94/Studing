import random
import os

os.system("cls")

numbers = []
number = number = str(random.randint(0,9))

for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

print("*"*60)
print("야구게임을 시작합니다!")

strike = 0
ball = 0
while strike < 3:
    strike = 0
    ball = 0
    num = str(input("숫자 3자리를 입력하세요: "))
    if len(num) == 3:
        for i in range(3):
          for j in range(3):
                if num[i] == numbers[j] and i == j:
                    strike += 1
                if num[i] == numbers[j] and i != j:
                    ball += 1
        
        if strike == 0 and ball == 0:
            print("Three OUT!")
        else:
            output = ""
            if strike > 0:
                output += "strike 개수: {} ".format(strike)
            if ball > 0:
                output += "ball 개수: {}".format(ball)
       
            print(output)

print("게임 성공!")