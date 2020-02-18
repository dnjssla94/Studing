# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
# 계속 더하는 프로그램을 작성해보자.

a = int(input())
b = 0
r = 0
for i in range(a):
    b += i
    r = i
    if b >= a:
        break
    

print(r)
