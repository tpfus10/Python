#리스트 복사하기 [:] 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\n My friend's favorite foods are: ")
print(friend_foods)

#리스트 얕은 복사(1차원에서 슬라이싱을 하지 않기 때문)
my_foods = friend_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#shallow copy 얕은 복사 (2차원에서는 슬라이싱할 경우 얕은 복사가 됨)
#2차원 리스트를 깊은 복사하려면 copy.deepcopy() 함수를 사용하면 됨
a1 = [[1,2,3],[4,5,6]]
b1 = a1[:]
print(b1) 
a1[0][0] = 100
print(a1)
print(b1)


#deep copy 깊은 복사 (1차원에서는 슬라이싱할 경우 깊은 복사가 됨)
a2 = [10, 20, 30, 40, 50]
b2 = a2[:]
print(b2)
a2[0] = 100
print(a2)
print(b2) #a의 값만 바뀌는 깊은 복사

a3 = [10, 20, 30, 40, 50]
b3 = a3[0:3] 
print(b3) 
a3[0] = 100
print(a3)
print(b3)
