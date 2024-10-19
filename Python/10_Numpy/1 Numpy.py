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

# 다차원 배열의 생성 2차원 배열 : 가로와 세로
array4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
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




# Numpy 배열의 arange()를 이용해 생성한 1차원 배열에 reshape(m, n)을 추가하면
# m * n 형태의 2차원 배열 (행렬)로 변경
# 주의할 점 : range()로 생성되는 배열의 원소 개수와 reshape(m, n)의 m * n의 개수가 같아야 한다.
array4 = np.arange(12).reshape(4, 3)  # 앞이 행, 뒤가 열
print(array4)

# Numpy 배열의 형태를 알기 위해서는 '.shape'를 실행
print(array4.shape)       # (4, 3)


# 1차원 배열의 경우 '(n, )' 처럼 표시
print(array1.shape)


# .linspace()

# 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 배열을 생성.
# arr_obj =np.linspace(start, stop, num)
# linspace()는 start부터 stop까지 num개의 배열을 같은 간격으로 생성
# num을 지정하지 않으면 50이 기본값.

array1 = np.linspace(1, 10, 10)
print(array1)


array2 = np.linspace(1, 10, 4)
print(array2)


array3 = np.linspace(0, np.pi, 20)      # numpy안의 pi(상수)를 지정해 동일한 간격으로 20개를 나눈 배열 생성
print(array3)


# 3) 배열의 데이터 타입 변환
# 배열은 숫자뿐만 아니라 문자열도 원소를 가질 수 있다.
array1 = np.array(['1.5', '0.62', '2', '3.15', '3.141692'])

print(array1)
print(array1.dtype)     # <U8 : 데이터 형식이 유니코드이며 문자의 수는 최대 8개 라는것을 의미.


# Numpy 데이터의 형식
# b : 물어본다 bool(boolean)
# i : 기호가 있는 정수 (signed) interger :
# u : 기호가 없는 정수 (unsigned) integer : 약 43억까지 가능
# f : 실수 floating-point (float)
# c : 복소수 . complex-floating gpoint
# M : 날짜 . datetime
# O : 파이썬 객체 (python) Objects
# U : 유니코드 Unicode, 유니코드 전에는 아스키 코드가 존재

# 배열이 문자열 (숫자 표시)로 되어 있다면 연산을 위해서는 문자열을 숫자 (정수나 실수)로 변환해야 한다.
# 형 변환은 asytype()로 가능
# num_arr = str_arr.astype(dtype)


str_array1 = np.array(['1.567', '0.123', '6.123', '9', '8'])
num_array1 = str_array1.astype(float)   # 실수 타입으로 바꾸겠다
print(str_array1)
print(num_array1)
print(str_array1.dtype)
print(num_array1.dtype)


# 정수를 문자열 원소로 갖는 배열을 정수로 변환
str_array2 = np.array(['1', '3', '5', '7', '9'])
num_array2 = str_array2.astype(int)
print(num_array2)
print(str_array2.dtype)
print(num_array2.dtype)

# 실수를 원소로 갖는 배열을 정수로 변환
num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
num_i1 = num_f1.astype(int)
print(num_i1) # 실수에서 정수로 형변환을 할 시 소수점은 내림 처리 시킴
print(num_f1.dtype)
print(num_i1.dtype)
