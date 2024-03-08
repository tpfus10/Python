def describe_pet (animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

#위치 인수(인수의 순서를 매개변수 순서와 맞추기)
#함수를 여러 번 호출하는 것도 가능함
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#키워드 인수(함수에 전달하는 이름-값 쌍)
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

#매개변수의 기본값
def describe_pet (pet_name, animal_type='bird'): #기본값이 있는 매개변수를 제일 뒤에 정의하기
    """반려동물 정보를 표시합니다"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet(pet_name='viola')
describe_pet('viola') #동일한 결과
describe_pet(animal_type='hamster', pet_name='harry')#인수를 명시적으로 전달할 경우 기본값을 무시