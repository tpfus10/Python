cars = ['audi', 'bmw', 'subaru', 'totyota']

#기본 예제
#조건 테스트(true나 false로 평가되는 표현식)->true는 if문 실행, false는 실행x
for car in cars:
    if car == 'bmw': #동등 연산자 ==는 일치하면 true, 불일치하면 false를 반환
        print(car.upper())
    else:
        print(car.title())


#여러 조건 확인하기
age = 12
if age < 4:
    print('입장료0$')
elif age <18:
    print('입장료 25$')
else:
    print('입장료 40$')        