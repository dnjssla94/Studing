#현재시간이 12시에서 1시 사이면 점심을 먹고 아니면 일한다.
time =12
seek =True
if 12 <= time < 1:
    print("점심먹으러감")
elif time >=15 and time <16 or seek:
    print("휴식시간")
else:
    print("working..")

#------------------------
a=10

if a>10:
    ret=100
else:
    ret = 500

ret = 100 if a > 10 else 500

#-----------------------
if a>10:
    ret=100
elif a==10:
    ret = 200
else:
    ret = 500
#둘다 F,F이면 get안에있는 기본 참값이 적용됨
ret = {a>10:100,a<10:500}.get(True,200)

#------------------------

name = "abcde"
if "a" in name:
    print("in")
else:
    print("not in")

 #------------------------