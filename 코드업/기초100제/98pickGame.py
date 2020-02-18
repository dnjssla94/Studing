# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

# 입력값의 정의역은 다음과 같다.

# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w

h, w = input().split()
n = int(input())

h = int(h)
w = int(w)
gameBoard = list()
for i in range(h):
    gameBoard.append([])
    for j in range(w):
        gameBoard[i].append(0)

sticks = list()
for i in range(n):
    l , d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    sticks.append((l,d,x,y))
print(sticks)
for i in range(n):
    if sticks[i][1] == 0:
        for j in range(sticks[i][0]):
            gameBoard[sticks[i][2]-1][sticks[i][3]-1+j] = 1
    elif sticks[i][1] == 1:
        for j in range(sticks[i][0]):
            gameBoard[sticks[i][2]-1+j][sticks[i][3]-1] = 1



for i in range(h):
    for j in range(w):
        print(gameBoard[i][j], end = ' ')
    print('')