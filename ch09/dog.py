#클래스 만들기
#self는 인스턴스 자기 자신을 의미함(모든 클래스의 함수는 self를 가짐)
#self는 필수 매개변수이며 반드시 맨 앞에 있어야 함
class Dog:
    """개를 표현하는 클래스"""
    def __init__(self, name, age): #__init__()은 생성자(앞뒤로 밑줄 두 개가 붙은 메서드는 파이썬이 자동으로 호출해줌)
        """name과 age 속성 초기화"""
        self.name = name #name과 age를 속성이라고 함(자바의 클래스 필드)
        self.age = age #속성은 self.으로 선언함
        #self.hello = '안녕하세요'->매개변수 없이 선언하는 속성이 있을 수 있음

    def sit(self): 
        """앉기"""
        print(f"{self.name} is now sitting.") #클래스 내에서 속성에 접근할 때는 'self.속성'형식

    def roll_over(self):  
        """구르기"""
        print(f"{self.name} is now rolled over!")

#클래스에서 인스턴스 만들기
#Dog의 인스턴스 생성, my_dog는 참조변수 역할
#인스턴스는 self를 통해 클래스의 속성과 메서드에 접근
#self는 자동으로 전달되기 때문에 직접 입력하지 않음
my_dog = Dog('Willie', 6) #생성자 호출>인스턴스 생성>__init__() 함수가 자동 호출
my_dog.sit() #클래스 바깥에서 속성에 접근할 때는 '인스턴스.속성' 형식
my_dog.roll_over()
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


#인스턴스 여러 개 만들기
your_dog = Dog('Lucy', 3)
your_dog.sit()
your_dog.roll_over()
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")

#위치 인수: 위치인수에서 리스트 언패킹을 사용하려면 *args를 사용
#매개변수에서 값을 가져오려면 args[0]과 같이 인덱스로 접근해야 함
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
print(maria.age)

#키워드 인수: 키워드 인수와 딕셔너리 언패킹을 사용하려면 **kwargs를 사용
#매개변수에서 값을 가져오려면 kwargs['name']과 같이 "키"값을 이용해 접근해야 한다.
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
print(maria2.address)

#비공개 메서드/속성 사용하기
#'__속성'이 비공개 속성 // '__속성__' 이 공개 속성
class Person:
    def __greeting(self): #비공개 메서드 선언
        print('Hello')

    def hello(self):
        self.__greeting()    # 클래스 안에서는 비공개 메서드를 호출할 수 있음
james = Person()
james.__greeting()    # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음

