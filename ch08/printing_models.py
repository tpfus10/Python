#함수 내부에서 리스트 수정하기1(함수를 사용하지 않은 버전)
 #출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
compeleted_models = []
 
 #남은 게 없을 때까지 디자인을 출력
 #출력한 디자인을 completed_models로 옮김
while unprinted_designs: #list가 null이면 false가 되어 끝남
    current_dsign = unprinted_designs.pop() #list의 pop은 끝에서 하나씩 제거
    print(f"Printing model: {current_dsign}")
    compeleted_models.append(current_dsign)

 #완료된 디자인 표시
print("\nThe following models have been printed:")
for completed_model in compeleted_models:
    print(completed_model)

#함수 내부에서 리스트 수정하기2(함수를 사용한 버전)
 #함수 생성하기
def print_models(unprinted_designs, completed_models): #list가 매개변수이면 mutable
    """
    남은 게 없을 때까지 디자인을 출력
    출력한 디자인을 completed_models로 옮김
    """
while unprinted_designs: #list가 null이면 false가 되어 끝남
    current_dsign = unprinted_designs.pop() #list의 pop은 끝에서 하나씩 제거
    print(f"Printing model: {current_dsign}")
    compeleted_models.append(current_dsign)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in compeleted_models:
        print(completed_model)

 #함수 호출하기
print_models(unprinted_designs, compeleted_models)
show_completed_models(compeleted_models)

#추가 실습: immutable 변수가 매개변수일 때
def modify_string(s): #스트링 값을 전달받음
    s += "world"       
    print(s)          #변수 s는 원래 변수 st가 가리키는 주소와 다름

st = "hello"
modify_string(st)     
print(st) #hello world가 아니라 hello가 나옴(immutable)

#함수가 리스트를 수정하지 못하게 하기(deepcopy와 shallowcopy)
unprinted_designs2 = ['phone case', 'robot pendant', 'dodecahedron']
deepcopy = unprinted_designs2[:]
shallowcopy = unprinted_designs2 
unprinted_designs2.append('airpods case')
print(deepcopy)
print(shallowcopy)