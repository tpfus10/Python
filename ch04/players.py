players = ['charles', 'martina', 'michael', 'florence', 'eli']

#양의 인덱스 사용하기
print(players[0:3]) #인덱스 0에서 2까지 출력
print(players[1:4])

#인덱스 생략하기
print(players[:3]) #첫 번째 인덱스를 생략하면 인덱스 0에서 시작하는 슬라이스가 됨
print(players[3:]) #마지막 인덱스를 생략하면 마지막까지 모두 포함하는 슬라이스가 됨

#음의 인덱스 사용하기1
print(players[-2:]) #뒤에서 두 번째부터 출력
print(players[:-2]) #뒤에서 두 번째까지 출력

#음의 인덱스 사용하기2
print(players[2:3]) #2만 출력 
print(players[2:-2]) #2만 출력 

#간격(step) 사용하기 -> [start:stop:step]
print(players[1:4:2]) #짝수 번째만 출력
print(players[::2]) # 0부터 2칸째마다 출력
print(players[::3]) # 0부터 3칸째마다 출력

#음의 간격(step) 사용하기
print(players[::-1]) #마지막부터 거꾸로 모두 출력
print(players[::-2]) #마지막부터 거꾸로 2칸째마다 출력

#슬라이스 순회하기
print("Here are the first three players on my team\:")
for player in players[:3]:
    print(player.title())