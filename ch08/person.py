#딕셔너리 반환하기 {key : value}
#키값은 index와는 다름(주소는 가지지만 순서가 의미 있는 인덱스값을 가지지는 않음)
def build_person(first_name, last_name, age=None): #None은 플레이스 홀더
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first': first_name, 'last' : last_name}
    if age: #None은 항상 false
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')#person이 딕셔너리이기 때문에 build_person을 호출하면 자동으로 musician도 딕셔너리가 됨
print(musician)