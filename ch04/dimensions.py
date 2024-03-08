#튜플의 정의(콤마로 정의, 괄호는 읽기 쉽게 하려고 쓰는 것)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#요소가 하나인 튜플의 정의
only_one = (3,)
print(only_one)

#튜플의 요소 변경 -> 불가능함
#dimensions[0] = 250

#리스트의 요소 병경 -> 가능함
dimen = [200, 50]
dimen[0]=250
print(dimen[0])

#튜플 순회하기
for dimensoin in dimensions:
    print(dimensoin)

#튜플 덮어쓰기(변경이 불가능하기 때문에 새 값을 할당하는 식으로 수정함)
dimensions = (250, 50)
print(dimensions[0])
print(dimensions[1])

#추가 개념1: 튜플과 함수
def test():
    return (10, 20)
a, b = test(); #튜플 값을 리턴
print(f"a= {a}, b= {b}")

#추가 개념2: 리스트와 enumerate 함수
lst = ['a', 'b', 'c', 'd']
for i, value in enumerate(lst): #리스트가 주어지면 인덱스와 값을 튜플에 저장
    print(f"i= {i}, value= {value}")


