# file = open("sample.txt", mode = "w",encoding = 'UTF-8')
# file.write("안녕 파이썬")
# file.close()

#rfile = open("sample.txt", mode="r",encoding = 'utf-8' )

# a = rfile.read(10)
# print(a)
# rfile.seek(0)#파일 포인터를 다시 처음으로
# a = rfile.read(10)
# print(a)
# rfile.close()


#with open("sample.txt", mode="r",encoding = 'utf-8' ) as file:
#    print(file.read()) #with문을 다 쓰고 빠져나가면 file은 자동소멸. 사용법이 간단하다.

with open("sample.txt", mode="r",encoding = 'utf-8' ) as s, open("sample2.txt", mode="w",encoding = 'utf-8' ) as t:
     t.write(s.read().replace("파이썬","Python"))