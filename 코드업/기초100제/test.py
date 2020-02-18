n = int(input())
whiteStone = list()
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    whiteStone.append((a,b))
print(whiteStone[1][1])