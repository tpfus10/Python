#합성(composition): 하나의 클래스를 여러 개의 클래스로 분리하기
#클래스 3은 클래스 1을 상속하며 클래스 2를 속성으로 사용함
#클래스1: Car Class
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

#클래스2: Battery Class
class Battery:
    """전기차의 배터리를 표현하는 클래스"""
    def __init__(self, battery_size=40): #배터리의 기본 사이즈를 40으로 설정
        """배터리 속성을 초기화"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """배터리의 크기를 설명하는 문장을 출력"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """이 배터리로 주행할 수 있는 거리를 알려줍니다"""
        if self.battery_size == 40:
            range = 150
        else:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

#클래스3: ElectricCar Class
class ElectricCar(Car): #'(부모 클래스)'를 붙여줘야 함(자바의 extends)
    """전기차에만 해당하는 특징을 정의"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화"""
        super().__init__(make, model, year) 
        self.battery = Battery() #Battery의 인스턴스를 생성, 인수가 없으므로 기본값 40이 배터리의 크기

my_leaf = ElectricCar('nissan', 'leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() #battery 속성의 describe_battery 메서드 호출
my_leaf.battery.get_range()

