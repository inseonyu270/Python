### Numpy ###
# : 배열 데이터를 효과적으로 다룰 수 있는 외부 모듈
# 2016년부터 파이썬이 본격적으로 핵심언어가 되기 시작


# Numpy를 이용하면 파이썬의 기본 데이터 형식과 내장 함수를 이용하는 것보다
# 다차원 배열 데이터를 효과적으로 처리할 수 있음.


# Numpy 홈페이지 : https://numpy.org

# 1. 배열 생성
# Numpy는 파이썬의 내장 모듈이 아니라서 별도로 설치
# pip install numpy

import numpy as np
print(np.__version__)

# 배열 Array이란 순서가 있는 같은 종류의 데이터가 저장된 집합
# Numpy를 이용해 배열을 처리하기 위해서는 우선 Numpy로 배열을 생성해야 한다.
# 다양한 방법으로 배열을 생성하는 방법 보기

# 1) 시퀀스 데이터로부터 배열 생성하기. array()
# 시퀀스 데이터 seq_data를 인자로 받아 Numpy의 배열 객체 (array object)를 생성
# arr_obj = np.array(seq.data)

# 정수 리스트로 배열 생성
data1 = [0, 1, 2, 3, 4, 5]
print(data1)            # 콤마(,)가 들어가 있으면 리스트            [0, 1, 2, 3, 4, 5]

array1 = np.array(data1)
print(array1)
print(array1.dtype)


# 정수와 실수가 혼합된 생성
data2 = [0.1, 5, 4, 12, 0.5]
array2 = np.array(data2)
print(array2)
print(array2.dtype)         # float64 : 정수와 실수가 혼합돼있을 경우 모두 실수로 변환
                            # (5fmf 5.0으로 받는다 한들 데이터 손해 X)
                            # 배열의 속성을 표현할 때는 np.array.속성과 같이 작성
                
array3 = np.array([0.5, 2, 0.01, 8])
print(array3)

# 다차원 배열의 생성 2차월 배열 : 가로와 세로
array4 = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(array4)

# 2) 범위를 지정해 배열 생성. arange()
# arange()를 이용해 Numpy 배열을 생성
# 파이썬의 range()와 사용방법이 비슷함.
# array_obj = np.arange(start, stop, step)
# start부터 시작해서 stop 전까지 step만큼 계속 더해 Numpy 배열을 생성
# start가 0인 경우 생략 가능
# step이 1인 경우에도 생략 가능

array1 = np.arange(0, 10, 2)                # 0부터 시작해서 10개 찍어내라 (9까지) 2칸씩 찍어라
print(array1)

array2 = np.arange(1, 10)
print(array2)

array3 = np.arange(5)
print(array3)

