n = input()
Li = list()
Li.extend(input().split())
result = list()
for i in range(len(Li)):
    result.append(int(Li[i]))
for i in range(len(result)):
    print(result[-1-i], end=' ')