
 # https://twinstarinfo.blogspot.com/2018/10/backjoon-15552-python.html
# flowerNum = int(sys.stdin.readline().rstrip())

# flowerLifes = list()


# for i in range(flowerNum):
#     startM, startD, endM, endD = sys.stdin.readline().rstrip()
#     # input().split()
#     startD = int(startD)
#     startM = int(startM)
#     endM = int(endM)
#     endD = int(endD)
#     a = (startM, startD, endM, endD)
#     flowerLifes.append(a)

# print(type(flowerNum))
# print(flowerLifes)

# a,b,c,d = sys.stdin.readline().split()
#     # print(t)
#     # if i == 0: a = t
#     # elif i == 1: b = t
#     # elif i == 2: c = t
#     # else: d = t
# print(a,b,c,d,'ss')
# print(type(a))
#-----------------------------------------------------
#-----------------------------------------------------
import sys
flowerNum = int(sys.stdin.readline())

flowerLifes = list()

for i in range(flowerNum):
    startM, startD, endM, endD = sys.stdin.readline().split()
    startD = int(startD)
    startM = int(startM)
    endM = int(endM)
    endD = int(endD)
    a = (startM, startD, endM, endD)
    flowerLifes.append(a)

count = 0
startMonth = 3
startDay = 1
mostLateMonth  = 0
mostLateDay = 0

def listSub(listA, listB):
    listC = list()
    for i in listA:
        if i not in listB:
            listC.append(i)
    return(listC)
def reduce(listA):
    listB = list()
    for i in range(len(listA)):
        a = listA[i][2:]
        listB.append(a)
    return listB

# 1. 최소 범위: 3 1 12 1 이므로 시작이 3 1 이 전인 것들중 가장 늦게 지는 꽃 선택
while True:
    choosen = list()
    cordinates = list()
    for i in range(len(flowerLifes)):
        if (flowerLifes[i][0]) < startMonth or (flowerLifes[i][0] == startMonth and flowerLifes[i][1] <= startDay):
            a = (flowerLifes[i][0],flowerLifes[i][1],flowerLifes[i][2], flowerLifes[i][3])
            cordinates.append(a)
    flowerLifes = listSub(flowerLifes, cordinates)

    cordinates = reduce(cordinates)
    cordinates.sort()
    choosen.append(cordinates[-1])
    startMonth = choosen[0][0]
    startDay = choosen[0][1]
    # print(choosen)
    count += 1
    if choosen[0][0] > 11:
        break
    elif len(flowerLifes) == 0 and choosen[0][0] < 12:
        count = 0
        break
    
print(count)

