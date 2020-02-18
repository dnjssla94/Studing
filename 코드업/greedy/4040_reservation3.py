peekDays , rooms = input().split()
peekDays = int(peekDays)    # 성수기 날 수
rooms = int(rooms)          # 방 개수
book = list()               # 예약 내역

for i in range(peekDays):
    rev = input()
    book.append(list(rev))

checkIn, checkOut = input().split()
checkIn = int(checkIn)
checkOut = int(checkOut)
enterDay = checkIn - 1  #인덱스와 동일.


def cntRoom(book, startDay, room) : # 그 룸에 startDay부터 머물 수 있는 날 수(길이) 반환
    length = 0
    if book[startDay][room] == 'X' : return(-1)
    else:
        while book[startDay][room] == 'O':
            startDay += 1
            length += 1
        return length

def maxCntRoom(book, startDay, rooms) :    # startDay부터 머물수 있는 길이가 가장 큰 방
    index = 0
    max = cntRoom(book, startDay, index)
    for i in range(rooms):
        if cntRoom(book, startDay, i) > max:
            index = i
            max = cntRoom(book, startDay, index)
    if index == 0 and cntRoom(book, startDay, index) == -1:    return(rooms + 1)
    else:   return index


count = 0
stay = maxCntRoom(book, enterDay, rooms)
for i in range(enterDay, checkOut - 2) :
    if stay == rooms + 1: 
        count = -1
        break
    elif cntRoom(book, i, stay) == -1:
        stay = maxCntRoom(book, i, rooms)
        count += 1
print(count)