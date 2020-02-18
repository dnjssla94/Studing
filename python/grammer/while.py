#반복문 while

guest = 1

while guest < 10:
    guest = guest + 1
    print("손님이 {}명 찼습니다.".format(guest))
    if guest ==10:
        print("손님이 꽉 찼습니다.")