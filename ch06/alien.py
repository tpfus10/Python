#딕셔너리 사용하기: 키-값 쌍의 컬렉션으로, 키를 이용해 값에 접근할 수 있음
#값에는 숫자, 문자열, 리스트, 다른 딕셔너리 등 파이썬에서 생성할 수 있는 모든 객체가 될 수 있음
allien_0 = {'color' : 'green', 'points' : 5}

#딕셔너리에 접근하기
print(allien_0['color'])
print(allien_0['points'])

new_points = allien_0['points']
print("You just earned {} points!".format(new_points))

#키-값 쌍 추가하기(딕셔너리가 동적 구조이기 때문에 가능)
allien_0['x_positon'] = 0
allien_0['y_positon'] = 25
print(allien_0) #딕셔너리는 정의된 순서대로 출력됨

#빈 딕셔너리로 시작하기
allien_1 = {}

allien_1['color'] = 'blue'
allien_1['points'] = 10

print(allien_1)

#딕셔너리 값 수정하기1
print("The alien is {}.".format(allien_1['color']))
allien_1['color'] = 'yellow'
print("The alien is {}.".format(allien_1['color']))

#딕셔너리 값 수정하기2
allien_2 = {'x_posiotion' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original positon: ({allien_2['x_posiotion'], allien_2['y_position']})")

##외계인을 오른쪽으로 이동(현재 속도에 따라 이동 거리 파악)
if allien_2['speed'] == 'slow':
    x_increment=1
elif allien_2['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3

##새 위치 출력하기
allien_2['x_posiotion'] += x_increment
print(f"New positon: ({allien_2['x_posiotion'], allien_2['y_position']})")

#키-값 쌍 제거하기: del문
#del문으로 제거한 키-값 쌍은 영구히 제거되기 때문에 잘 사용하지 않음
del allien_2['speed']
print(allien_2)

