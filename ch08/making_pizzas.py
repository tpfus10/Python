#전체 모듈 임포트하기
#임포트 하기 전에 함수만 저장된 모듈이 있어야 함
#import문을 써주고 함수 앞에 "파일명."을 붙여줘야 함
import pizza_c

pizza_c.make_pizza2(16, 'pepperoni')
pizza_c.make_pizza2(12, 'mushrooms', 'greeen peppers', 'extra cheese')


#특정 함수 임포트하기
#from 모듈명 import 함수명 형식
#모듈에서 필요한 함수를 콤마로 구분해서 원하는 만큼 임포트할 수 있음
#함수 앞에 "파일명."을 붙이지 않아도 됨
from pizza_c import make_pizza2

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'greeen peppers', 'extra cheese')

#함수를 임포트해서 별칭 부여하기
#별칭으로 함수를 호출할 수 있음
from pizza_c import make_pizza2 as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'greeen peppers', 'extra cheese')

#모듈에 별칭 부여하기
#모듈에 별칭을 부여하더라도 모듈의 함수는 원래 이름을 유지함
import pizza_c as p

p.make_pizza2(16, 'pepperoni')
p.make_pizza2(12, 'mushrooms', 'greeen peppers', 'extra cheese')

#모듈의 모든 함수를 모두 임포트하기
#from~import 문 끝에 *를 쓰기
#함수 앞에 "파일명."을 붙이지 않아도 됨
from pizza_c import *

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'greeen peppers', 'extra cheese')

