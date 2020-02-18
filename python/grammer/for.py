#반복문 for

a = ["python","java","C++","javascript"]
for i in a:
    print(i)

#----------------------

for i in range(0,11,2):
    print(i) 

#------------------
print("\n")
a=[(1,2),(3,4),(5,6)]
for i in a:
    for j in i:
        print(i)
        print(j)

#--------------------

student = [{"홍길동":100},{"가제트":200},{"가가멜":300}]
for s, i in enumerate(student,start=1):
    
    print(s,list(i.items())[0])
    data = list(i.items())[0]
    name = data[0]
    value = data[1]
    print("이름: {}, 점수: {}".format(name,value))

#---------------------
msg = "python programming"

for s, i in enumerate(msg, start=1):
    print(s, i)

#----------------------

result =[]
for num in range(1,6):
    result.append(num+5)
print(result)
#이걸 list comprehension으로 표기해보자 
# 순서: 실행 반복 조건 
result = [num + 5 for num in range(1,6)]
print(result)
#list comprehension 표기:
result = [num+5 for num in range(1,11) if num % 2 ==0]
print(result)
#list comprehension 표기:
result = [num*3 for num in range(1,100) if num % 2 ==0]
print(result)


#list comprehension 표기: 구구단
for i in range(2,10):
    for j in range(1,10):
        result=i*j
        print ("{} * {} = {}".format(i,j,result))

gugudan = ["{} * {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
print(gugudan)
#-------------------
