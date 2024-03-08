magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that was a great trick!') 
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
#for 라인 안에 있어야 반복함(이를 루프 블록이라고 함)
#cmd에서는 ... 점 세 개 뒤에 한 칸을 띄워야 for문에 포함됨(아무것도 입력하지 않고 엔터키를 누르면 for문이 실행됨)
print('Magic is over\n')

for magician in magicians:
    print(magician)
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
    for magician in magicians:
        print(magician)