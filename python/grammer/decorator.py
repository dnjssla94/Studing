#decorator
#이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

#파이썬에서 함수는 일급 객체
#클로저 사용
#함수내 함수를 정의할 수 있음

# def outer_function(msg):
#     def inner_function():
#         return "난 내부함수인데 {}를 받았어.".format(msg)
#     return inner_function


# c = outer_function("HelloUU")
# #print(dir(c))
# print(c.__closure__[0].cell_contents)

#-------------------------------------------

# import time

# def time_checker(func):
#     def inner_function(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("함수: {}, 동작시간: {}".format(func.__name__, end_time-start_time))
#         return result
#     return inner_function


# @time_checker     #이게 바로 데코레이터. test1은 런타임때 
# def test1():      #time_checker의 인자가 되고 실제로는 time_checker가 시행된다.
#     for i in range(5):
#         time.sleep(0.1)

# @time_checker
# def test2():
#     for i in range(3):
#         time.sleep(0.1)

# test1()
# test2()

#-------------------------------------------

# from functools import wraps

# def login_required(func):
#     @wraps(func)
#     def inner_function(*args, **kwargs):
#         if not kwargs.get("is_login"):
#             print("로그인이 되지않아 수행하지 못힙니다.")
#             return
#         return func(*args, **kwargs)
#     return inner_function

# @login_required
# def login():
#     '''로그인 테스트 함수입니다.'''
#     print("안녕")
#     return "is_login"

# print(login.__name__)
# print(login.__doc__)
# login()

#--------------------------------------

from functools import wraps

def login_required(func):
    @wraps(func)
    def inner_function(*args,**kwargs):
        if not kwargs.get("is_login"):
            print("{}님, 로그인이 되지않아 수행하지 못힙니다.".format(args))
            return
        return func(*args, **kwargs)
    return inner_function

@login_required
def login(*args):
    '''로그인 테스트 함수입니다.'''
    print("{}님 로그인 확인되었습니다.".format(args))
    return "is_login"

print(login.__name__)
print(login.__doc__)
login("요를레히히")

#----------------------------------------------

def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "{}/{}/{}".format(new_args,func(name),new_args)
        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return "방가워" + msg

print(test("홍기르똥이"))