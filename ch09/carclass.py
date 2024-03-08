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

       
       
class Battery:
    """전기차의 배터리를 표현하는 클래스"""
    def __init__(self, battery_size=40): 
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


class ElectricCar(Car): 
    """전기차에만 해당하는 특징을 정의"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화"""
        super().__init__(make, model, year) 
        self.battery = Battery() 