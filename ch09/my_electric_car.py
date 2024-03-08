#모듈에 여러 클래스 저장하기(car+electriccar+battery)
#from carclass import ElectricCar

#별칭을 사용해서 클래스 임포트하기
from carclass import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', '2024') 
print(f"My car is {my_leaf.get_descriptive_name()}")
print("My car is {}".format(my_leaf.get_descriptive_name()))
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

#별칭을 사용해서 모듈 임포트하기
import carclass as cc
my_leaf2 = cc.ElectricCar('nissan', 'leaf', '2024') 
print(f"My car is {my_leaf2.get_descriptive_name()}")
