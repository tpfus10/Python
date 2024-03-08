#단일 클래스 임포트하기
from carclass import Car

my_new_car = Car('audi', 'a4', 2024)
print(f"My new car is {my_new_car.get_descriptive_name()}.")

my_new_car.odometer_reading = 23
my_new_car.read_odometer() 

