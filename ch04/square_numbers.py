#squares_set = {} {}기호를 사용했기 때문에 set 변수임

squares = [] #[]기호를 사용했기 때문에 list 변수임
for value in range(1,11):
    #square = value ** 2
    squares.append(value ** 2)

print(squares)
print(value) #파이썬에서는 지역변수의 개념이 없음