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

def maxCntRoom(book, startDay, rooms) :    # startDay부터 머물수 있는 길이가 가장 큰 방의 머물수있는 날 수
    length = -1
    result = -1
    for i in range(rooms):
        result = cntRoom(book, startDay, i)
        
        if result > length:
            length = result
    if length != -1:    return(length)
    else:   return(-1)

def conclusion(enterDay, checkOut):
    count = 0
    while enterDay < checkOut - 2 :
        length = maxCntRoom(book, enterDay, rooms)
        enterDay = enterDay + length
        count += 1
        if length == -1: 
            count = 0
            break
    return (count - 1)

c = conclusion(enterDay, checkOut)
print(c)    