try:
    file = open("sample.txt","r") 
    val = "10.5"
    n = int(val)
    # idx = []
    # idx[0] = 100
# except ValueError as e:
#     print("오류발생 {}".format(e))
# except IndexError as e:
#     print("오류발생 {}".format(e))


# except Exception as e:
#     print("오류발생 {}".format(e))

# except:
#     pass
# print("OK")#막강하나 남발하면 안됨.

except:
    print("오류발생")
finally:
    file.close()
    print("정상 동작 확인")