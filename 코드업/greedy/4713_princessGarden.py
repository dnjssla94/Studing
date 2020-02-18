# 오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.

# 총  N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 
# 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 
# 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4,6,9,11월은 30일까지 있고, 
# 1,3,5,7,8,10,12월은 31일까지 있으며, 2월은 28일까지만 있다.)
# 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
# 1. 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
# 2. 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다.
#  N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 
#  꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오.


# input을 바꿔보자....


flowerNum = int(input())

flowerLifes = list()

for i in range(flowerNum):
    startM, startD, endM, endD = input().split()
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