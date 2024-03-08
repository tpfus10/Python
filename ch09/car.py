#클래스의 기본 속성 설정하기
class Car:
    """자동차를 표현하는 클래스"""
    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #매개 변수 없이 선언하는 기본 속성

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        
    def read_odometer(self):
        """자동차의 주행거리를 출력"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # 속성값 수정하기2의 메서드
        """
        거리계를 주어진 값으로 설정
        현재 값보다 적은 값을 할당할 수 없음
        """
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles): # 속성값 수정하기3의 메서드
        """거리계 값을 주어진 값만큼 늘림"""
        self.odometer_reading +=miles

    def fill_gas_tanks(self):
       """연료가 남은 양을 출력합니다"""
       self.gas = 20
       print("This car have {self.gas} gas!")

my_new_car = Car('audi', 'a4', 2024)
print(f"My new car is {my_new_car.get_descriptive_name()}.")
my_new_car.read_odometer()

#속성값 수정하기1: 속성 값 직접 수정하기(클래스 외부에서)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#속성값 수정하기2: 메서드를 통해 속성 값 수정하기
my_new_car.update_odometer(24)
my_new_car.read_odometer()

#속성값 수정하기3: 메서드를 통해 속성 값 증가시키기
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#클래스 상속
class ElectricCar(Car): #'(부모 클래스)'를 붙여줘야 함(자바의 extends)
    """전기차에만 해당하는 특징을 정의"""

    def __init__(self, make, model, year): #자식 클래스의 __init__() 메서드
        """부모 클래스의 속성을 초기화"""
        super().__init__(make, model, year) 
        self.battery_size = 40 #자식 클래스의 속성 정의

    def describe_battery(self): #자식 클래스의 메서드 정의 
        """배터리의 크기를 설명"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tanks(self):
       """전기차에는 연료통이 없습니다."""
       print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

#자식 클래스의 속성과 메서드 정의
my_leaf.describe_battery()

#부모 클래스의 메서드 오버라이드
my_leaf.fill_gas_tanks()


