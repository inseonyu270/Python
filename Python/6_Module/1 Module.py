### 모듈 ###
# 1. 모듈이란?
# 한마디로 파이썬 파일(.py)
# 언제든지 사용할 수 있도록 변수나 함수 또는 클래스를 모아 놓은 파일

# 2. 모듈 생성
# converter.py 생성

# 3. 모듈의 사용
# 반드시 같은 디렉터리에 있어야 한다.
# 모듈에 저장된 함수를 사용하는 방법

# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때
# 예) import 모듈



import converter

miles = converter.kilometer_to_miles(150)       # 모듈명.함수명() 형식으로 호출
print(f'150KM = {miles}miles')                  # 150KM = 93.20565miles

pounds = converter.gram_to_pounds(1000)
print(f'1000gram = {pounds}pounds')             # 1000 gram = 2.206 pounds

print()




# 2) 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법
## 하나의 함수를 불러올 때 ##
# 예) from 모듈 import 함수

## 하나 이상의 함수를 불러올 때 ##
# 예) from 모듈 import 함수1, 함수2

## 모듈 안에 있는 함수를 다 가지고 오고 싶을 때
# 예) from 모듈 import * (* : 모든 함수)

from converter import kilometer_to_miles        # 모듈은 가지고 오지 않고 특정 함수만 가져옴.


miles = kilometer_to_miles(150)
print(f'150KM = {miles}miles')  
print()


from converter import *                         # 모듈은 가져오지 않고 모듈의 모든 함수 가져옴


pounds = gram_to_pounds(1000)                   # 모듈명을 명시하지 않고 사용
print(f'1000 gram = {pounds}pounds')

# 3. 별명 사용하기
# 모듈이나 함수를 import 하는 경우에 원래 이름 대신 별칭 alias를 지정하고  사용
# 모듈이나 함수의 이름이 긴 경우에 주로 짧은 별명을 지정하고 긴 본래 이름 대신 사용 가능
# 별명을 지정할 때는 as 키워드를 사용

print()

import converter as cvt             # converter 모듈에 cvt라는 별명을 지정
miles = cvt.kilometer_to_miles(150)         # 별명을 이용해서 함수 사용
print(f'150KM = {miles}miles')

print()

from converter import kilometer_to_miles as k_to_m  # 함수에도 별명을 지정 가능
miles = k_to_m(150)                                 # 함수 이름 대신 별명을 사용
print(f'150KM = {miles}miles')

