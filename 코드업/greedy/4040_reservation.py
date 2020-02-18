peekDays , rooms = input().split()
peekDays = int(peekDays)    # 성수기 날 수
rooms = int(rooms)          # 방 개수
book = list()               # 예약 내역

allX = list()
for i in range(rooms):
    allX.append('X')
for i in range(peekDays):
    rev = input()
    book.append(list(rev))

checkIn, checkOut = input().split()
checkIn = int(checkIn)
checkOut = int(checkOut)
enterDay = checkIn - 1
break2 = False
cnt = 0
tempDay = 0

for i in range(enterDay ,checkOut - 2 ):    #예약불가능할때 종료.
    if book[i] == allX:
        print(-1)
        break2 = True
        exit()

while enterDay != checkOut - 2:

    tmpNum = 0
    for i in range(rooms):
        for j in range(enterDay, checkOut -1):
            tempDay = j
            if book[j][i] == 'X':
                break
        if tmpNum < tempDay:
            tmpNum = tempDay
    enterDay = tmpNum

    cnt += 1
print(cnt-1)
