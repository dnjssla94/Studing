# 냉난방기가 멀리 있어서 리모컨으로 조작하려고 하는데, 리모컨의 온도 조절 버튼은 다음과 같다.
# 1) 온도를 1도 올리는 버튼
# 2) 온도를 1도 내리는 버튼
# 3) 온도를 5도 올리는 버튼
# 4) 온도를 5도 내리는 버튼
# 5) 온도를 10도 올리는 버튼
# 6) 온도를 10도 내리는 버튼
# 이와 같이 총 6개의 버튼으로 목표 온도를 조절해야 한다.
# 현재 설정 온도와 변경하고자하는 목표 온도가 주어지면 이 버튼들을 이용하여 목표 온도로 변경하고자 한다.
# 이 때 버튼 누름의 최소 횟수를 구하시오.
# 예를 들어, 7도에서 34도로 변경하는 경우,
# 7 -> 17 -> 27 -> 32 -> 33 -> 34
# 이렇게 총 5번 누르면 된다.

currentTemp, goalTemp = input().split()
currentTemp = int(currentTemp)
goalTemp = int(goalTemp)

cnt = 0

if goalTemp >= currentTemp:
    gap = goalTemp - currentTemp
    while gap > 7 :
        if goalTemp > currentTemp:
            currentTemp += 10
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 10
            cnt += 1
        gap = abs(goalTemp - currentTemp)

    while gap > 2.5:
        if goalTemp > currentTemp:
            currentTemp += 5
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 5
            cnt += 1
        gap = abs(goalTemp - currentTemp)

    while gap != 0:
        if goalTemp > currentTemp:
            currentTemp += 1
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 1
            cnt += 1
        gap = abs(goalTemp - currentTemp)

else:
    gap = currentTemp - goalTemp
    while gap > 7 :
        if goalTemp > currentTemp:
            currentTemp += 10
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 10
            cnt += 1
        gap = abs(goalTemp - currentTemp)

    while gap > 2.5:
        if goalTemp > currentTemp:
            currentTemp += 5
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 5
            cnt += 1
        gap = abs(goalTemp - currentTemp)

    while gap != 0:
        if goalTemp > currentTemp:
            currentTemp += 1
            cnt += 1
        elif goalTemp < currentTemp:
            currentTemp -= 1
            cnt += 1
        gap = abs(goalTemp - currentTemp)

print(cnt)
