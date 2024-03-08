#인수를 임의의 개수로 전달하기: 함수가 받는 인수 개수를 미리 알 수 없을 때
#매개변수 앞에 *을 써주면 이 함수가 전달받는 매개변수명의 튜플에 모음
def make_pizza(*toppings):
    """요청받은 토핑 리스트를 출력합니다."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'greeen peppers', 'extra cheese')

#위치 인수와 임의 인수를 같이 쓰기(*args)
#여러 인수를 받을 때 임의 인수는 반드시 마지막에 배치해야 함
def make_pizza2(size, *toppings):
    """주문 내용을 요약합니다."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'greeen peppers', 'extra cheese')