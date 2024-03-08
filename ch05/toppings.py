requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#특별한 요소 확인하기
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

#리스트가 비어있는지 확인하기(for 루프를 실행하기 전에 먼저 확인하는 것이 좋음)
#if문과 빈 컨테이너(빈 문자열/list/tuple/set)
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
        print('\nFinished making your pizza!')
else:
    print("\nAre you sure you want a plain pizza?")

#여러 개의 리스트 다루기
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')
