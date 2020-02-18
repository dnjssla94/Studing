# 입력 예시   
# 5
# 1 2 3 4 5

# 출력 예시
# 1
# 2
# 3
# 4
# 5

a= int(input())
li = list()
li.extend(input().split())
re = list()
for i in li:
    re.append(int(i))
for i in re:
    print(i)