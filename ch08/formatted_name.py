#단순한 값 반환하기(파이썬에서는 반환타입을 자동으로 정함)
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#인수를 옵션으로 만들기: 매개변수의 디폴트값을 공백으로
def get_formatted_name(first_name, last_name, middle_name=' '):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    if middle_name: #middle_name이 있으면 true가 됨
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee') #파이썬은 비어 있지 않은 문자열을 true로 해석함
print(musician)
