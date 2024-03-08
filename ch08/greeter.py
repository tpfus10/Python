#함수 정의하기
#첫 줄 이후로는 함수의 바디
#독스트링(함수 정의 바로 뒤, 함수에 대한 문서 생성, 보통 세 개의 따옴표로 감싸줌)
def greet_user(): 
    """단순한 인사말을 표시합니다""" 
    print("Hello!")

#함수 호출
greet_user() 
help(greet_user) #독스트링을 출력
print(greet_user.__doc__) #독스트링을 출력


#함수에 정보 전달하기(파이썬은 리턴 타입을 자동으로 정함)
def greet_user(username): 
    """단순한 인사말을 표시합니다""" 
    print(f"Hello,{username.title()}")
    username = 'kim' #string은 immutable하기 때문에 'jesse'그대로 출력됨
greet_user('jesse') 

#immutable한 변수에 값을 덮어쓰면 값이 달라지는 것이 아니라 다른 주소에 새로운 값이 저장됨
#ex. input_name=kim input_name=hong -> kim과 hong이 각각  다른 주소에 저장됨

#while 루프와 함수
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == q:
        break

    l_name = input("Last name:")
    if l_name == q:
        break

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
