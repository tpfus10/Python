def ten_times(func):
    for i in range(5):
        func()

def print_hello():
    print('hello')

ten_times(print_hello)

def print_work():
    print('coding')

ten_times(print_work)

#더하기 함수
def add(x, y):
    return x+y

#빼기 함수
def minus(x, y):
    return x-y

#함수와 인수를 함께 전달
def apply_operation(operation, x, y):
    return operation(x,y)

result1 = apply_operation(add, 3, 4)
print(f"add 결과: {result1}")
result2 = apply_operation(minus, 3, 4)
print(f"minus 결과: {result2}")

#map/filter 함수의 활용(apply_operation과 동일한 역할)
# def power(item):
#     return item*item

# def under_three(item):
#     return item < 3

#람다식으로 map/filter 함수 표현하기
power = lambda x: x*x
under_three = lambda x: x<3

#map 함수: map(함수, 리스트나 튜플)
lst = [1, 2, 3, 4, 5]
map_list = map(power, lst)
print(f"map() 함수 적용결과: {list(map_list)}") #list를 함께 써줘야 함

#filter 함수: filter(함수, 리스트나 튜플)
filter_list = map(under_three, lst)
print(f"map() 함수 적용결과: {list(filter_list)}") #list를 함께 써줘야 함



