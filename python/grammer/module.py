
#파이썬 클레스의 멤버 변수와 함수에는 항상 self가 붙어야한다.
#double underbar는 외부에서 접근 못하는 함수를 표시하는 약속
class FishCakeMaker:
    def __init__(self, **kwargs):#생성자. 클래스 내의 함수는 self가 반드시 있어야함.
        self.size = 10
        self.flavor = "red bin"
        self.price = 100
        if "size" in kwargs:
            self.size = kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")

    # def __del__(self):#소멸자
    #     print("삭제되었습니다.")

    def __lt__ (self,other): #연산자 오버로딩
        return self.price < other.price
    def __le__ (self,other): #연산자 오버로딩
        return self.price <= other.price
    def __gt__ (self,other): #연산자 오버로딩
        return self.price > other.price
    def __ge__ (self,other): #연산자 오버로딩
        return self.price >= other.price
    def __eq__ (self,other): #연산자 오버로딩
        return self.price == other.price
    def __ne__ (self,other): #연산자 오버로딩
        return self.price != other.price

    def __str__(self):#__str__: 객체를 프린트하면 출력
        return "class fishCakeMaker (size: {}, price: {}, flavor: {})".format(self.size,self.price,self.flavor)
   

   
    def show(self):
        print("붕어빵 종류 {}".format(self.flavor))
        print("붕어빵 크기 {}".format(self.size))
        print("붕어빵 가격 {}".format(self.price))
        print("*"*60)

class MarketGoods(FishCakeMaker):#상속
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)#부모클래스 생성자 호출 꼭 해주자
        self._market_price = self.price+margin
    
    def show(self):
        print(self.flavor,self._market_price)

print(__name__)
if __name__ == "__main__":
    print(__name__)
    fish1 = MarketGoods(size = 25, price = 400)
    fish1.show()  

def add(a,b):
    return a+b