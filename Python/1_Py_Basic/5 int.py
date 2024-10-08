### 자료형 ###
# 프로그래밍을 할 때 쓰이는 숫자 ,문자열 등 자료형태로 사용하는 모든 것

# 다른 언어의 경우에는 변수를 설정 시에 자료형을 설정해야 하는 경우가 많다.
# 파이썬은 자료형을 따로 설정하지 않아도 대입되는 값( value, Data )에 따라서 자료형이 결정된다.


# 정수 int

# int() 함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환이 가능하다.
print(int(1.9))         # 1 // 1.9의 소수점(.9) d이하를 제거하여 정수 1로 변환
print(int(True))        # 1 // True는 1로 변환
print(int(False))       # 0 // False는 0으로 변환
print(int('100'))       # 100 // 문자열 '100'을 정수 100으로 변환
print(type(1.9))        # type() : 안에 들어간 내용의 데티어 타입을 알아 볼 수 있다.

# 10인주슬 2진수, 8진수, 16진수로 변환하는 방법
print()
n = 10
print(type(n))
print(bin(n))   # 2진수로 변환
print(oct(n))   # 8진수로 변환
print(hex(n))   # 16진수로 변환

