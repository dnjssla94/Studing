import os

while True:
    os.system("cls")
    s = input("계산기 만들기: ")
    print("결과: {}".format(eval(s)))
    os.system("pause")