n = int(input())
whiteStone = list()
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    whiteStone.append((a,b))

badukBoard = list()
for i in range(19):
    badukBoard.append([])
    for j in range(19):
        badukBoard[i].append(0)

for i in range(n):
    badukBoard[whiteStone[i][0]-1][whiteStone[i][1]-1] = 1

for i in range(19):
    for j in range(19):
        print(badukBoard[i][j], end = ' ')
    if i == 18:
            break
    else:
        print('')