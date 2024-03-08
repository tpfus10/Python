#모듈에서 여러 클래스 임포트하기
from carclass import Car, ElectricCar

#모듈에서 모든 클래스 임포트하기(잘 사용하지 않음)
# from carclass import *

my_mstang = Car('ford', 'mustang', 2024)
print(my_mstang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())