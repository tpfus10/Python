class Shape:
    def __init__(self, base, height):
        self.__base = base
        self.height = height

    #getter/setter의 정의(decoration의 사용)
    @property #decorator for getter
    def get_base(self):
        return self.__base
    
    @height.setter
    def height(self, vlaue):
        self.__height = value

    def get_data(self):
        return 1, 2, 3

shape = Shape(10, 30)
print(shape.height(50))

_, a, b = shape.get_data() # '_'은 무시하겠다는 의미 (2, 3만 저장)

a=[1, 2, 3]
b=[11, 22, 33]

#리스트 병합
mylist = [*a,*b]
print(mylist)

#zip 함수
c=['a', 'b']
z=zip(a,c)
print(list(z)) # 요소가 2개만 짝지어져서 출력됨

