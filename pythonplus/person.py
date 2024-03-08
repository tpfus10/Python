class Person:
    count = 0 #클래스 변수(클래스 내에 있지만 함수 밖에 있음)
    #__init__: 생성자
    def __init__(self, name, age, address):
        self.name = name #인스턴스 변수(함수 내에 있음, 'self.'을 붙임)
        self.age = age
        self.address = address
        self.list = ['a', 'b', 'c', 'd'] 
        self.__vision = 1.0 #private 속성
        self.weight = 70 
        self.height = 1.7
        print("객체 {} 생성되었습니다.".format(self.name))
        #클래스 변수를 증가
        Person.count += 1 #파이썬은 count++ 없음

    #클래스 메소드 생성
    @classmethod #decorator(자바의 annotation)
    def printing(cls):
        print("객체의 수: {}".format(cls.count))
    
    #__call__: 클래스의 객체를 호출하게 해주는 메서드
    def __call__(self):
        return self.weight/(self.height*self.height)

    #__eq__: 객체의 속성을 비교할 때 사용(T/F)
    def __eq__(self, other):
        #return self.age == other.age
        return self.address == other.address

    #__len__: 객체의 길이를 출력할 때 사용
    def __len__(self):
        return len(self.list)

    #__str__: 객체를 String으로 출력할 때 사용
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.age, self.address)

    #private 속성은 클래스 내에서 함수를 생성해서 사용해야 함
    def show_person_vison (self):
        print("The person's vision is {}".format(self.__vision))

    #__del__: 소멸자(프로그램이 종료되면 자동으로 실행됨)
    def __del__(self):
        print("객체 {}이 소멸되었습니다.".format(self.name))

new_person = Person('hong', 20, 'pusan')
print("The person's name is {}".format(new_person.name))
print(f"The person's weight is {new_person.weight}.")

#같은 메소드지만 호출방법이 다름: 객체.메소드 vs 메소드(객체)
new_person.show_person_vison() #(show_person_vison 메소드 호출)
print(str(new_person)) #객체를 String으로 출력(str 메소드 호출)
print(new_person.__str__()) #이것도 가능하긴 함
print(new_person) #print는 String을 요구하기 때문에 자동으로 str이 호출됨
print(len(new_person))

#속성값을 n자리 너비로 출력, 오른쪽 정렬, 부족한 자리는 공백으로 채움
print(f"The age of new_person is {new_person.age:5}")

#type 함수: 객체의 데이터 타입을 확인할 수 있는 함수
print("The data type of this object is{}.".format(type(new_person)))

#isinstance 함수: 객체가 해당 클래스의 객체인지 확인할 수 있는 함수
print("The 'new_person' is object of 'Person': {}.".format(isinstance(new_person, Person)))

#private 속성이라 클래스 밖에서 사용 불가능함
#print("The person's vision is {}.".format(new_person.__vision))

#__eq__ 메소드를 호출: '객체1 == 객체2'
other_person = Person('kim', 20, 'seoul')
print(new_person == other_person)

#__call__메소드호출
print(f"BMI 지수: {new_person()}")

#__del__메소드의 역할: 삭제해야 하는 객체를 자동으로 삭제해줌
Person('guest', 14, 'jeju') #참조변수가 없는 객체는 가비지 컬렉션의 대상이 됨(생성되고 바로 삭제됨)

#클래스 변수의 활용: '클래스명.변수명' 
print(f"객체가 생성되었습니다 : {Person.count} 개")
print(f"객체가 생성되었습니다 : {new_person.count} 개")
print(f"객체가 생성되었습니다 : {other_person.count} 개")
#->세 가지 형식이 모두 가능함(클래스 변수는 함수들이 모두 같이 공유함)

#클래스 메소드 호출
Person.printing()

#__getitem__: 클래스의 인덱스에 접근할 때 자동으로 호출되는 메서드
class Test:
    def __init__(self): ##self = a
        print("TEST 함수의 생성자 입니다.")
        self._numbers = [n for n in range(1, 11)]

    def __getitem__(self, index):
        print("__gettiem__메서드 호출")
        return self._numbers[index]
    
a  = Test() # Test 클래스 객체 생성
print(f"The forth number is {a[3]}.") # __gettiem__메서드 호출: '객체[인덱스]'

