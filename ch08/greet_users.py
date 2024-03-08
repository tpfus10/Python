#다양한 형태의 변수를 함수의 매개변수로 전달할 수 있음 
#mutable과 immutable: 이 속성에 따라 변수가 함수의 매개변수로 전달될 때 원래 입력 변수값이 변경되는지 안되는지 결정됨
#mutable: list, dictionary
#immutable: 문자형, 숫자형, tuple, boolean

#함수에 리스트 전달하기
def greet_uers(names):
    """리스트의 사용자에게 단순한 인사말을 출력합니다"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_uers(usernames)