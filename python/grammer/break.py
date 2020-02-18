

num =0
while True:
    print (num)
    num +=1

    if num==20:
        break

#----------------

# for i in range(1,100):
#     for j in range(1,100):
#         print(i,j)
#         if j == 10:
#             break

#------------------
num =0
while num < 10:
    num +=1
    if num ==5:
        continue
    print(num)

#----------------

point = [80,100,50,40,60]

for p in point:
    if p<70:
        continue
    print("{}점 입니다.".format(p))

#====------------------

hap = 0
for i in range(1,100):
    if i%2==0:
        continue
    hap += i
print ("홀수의 합: %d"%hap)