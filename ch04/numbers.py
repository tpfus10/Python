#리스트의 덧셈
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

#리스트의 뺄셈(- 기호를 사용하지 않음)
a = [1, 2, 3, 4]
b = [3, 4]
c1 = list(set(a)-set(b)) #set에는 - 기호를 사용할 수 있음(set으로 계산하고 다시 리스트로)
print(c1)

#리스트의 곱셈
d = [0]
e = d*5
print(e)

#2차원 리스트
matrix = [[3, 7, 9],
		  [4, 2, 6],
	   	  [8, 1, 5]]
print(matrix[2][0]) 

#for문: 문자열, range, tuple (리스트의 다양한 형태)
for g in 'fghij':
    print(g)
    
for h in range(1, 6):
    print(h)
    
for i in (1, 2, 3, 4, 5):
    print(i)

f = 'abcde' #리스트는 슬라이싱도 모두 적용 가능함
print(f[:2])