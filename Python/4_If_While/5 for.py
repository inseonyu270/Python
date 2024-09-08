# for 문
# 값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문
# 1) 특정 횟수 반복
# 2) 데이터 순회


# 기본 구조
# for 변수 in 반복가능 객체:
#   반복실행문

# for n in [2, 4, 6]:       #반복될 때 마다 순서대로 전달
#   print(n)


# 반복가능 객체 #
# 1. 시퀀스 자료형 : 순서를 가지고 있는 자료형
# 문자열, 리스트, 튜플, range


# 1-1) 문자열
# for 문자 in 문자열 :
#   반복 실행문

# for ch in 'hello':
#   print(ch)

# 1-2) 리스트
# for 요소 in [리스트]:
#   반복 실행문

# for item in ['가위', '바위', '보']:
#   print(item)



### 리스트 내포 ###
# 리스트를 생설할 때 for문을 유용하게 사용할 수 있다.

## 기본 형식 ##
# 리스트 = [표현식 for 변수 in 반복가능객체]

li = [n * 2 for n in [1, 2, 3]]
print(li)

# 조건에 맞는 데이터만 추출 가능
li = [n * 2 for n in [1, 2, 3, 4, 5] if n % 2 == 1]
print(li)


# 1-4) range()함수
# 정수 범위를 만들어 낼 때 유용한 함수

## 기본 구조 ##
# range(초기화, 종료값, 증감값)

# 특징
# 1. 초기값부터 종료값 전까지 숫자(n)들의 컬렉션을 만듦 (초기값 <= n < 종료값)
# 2. 초기값을 생략하면 0부터 시작
# 3. 종료값은 생략 X
# 4. 증감값을 생략하면 1씩 증가

for n in range(1, 11, 2):
    print(n)
    
for i in range(10):         # 10번 반복
                            # 초기값 : 0
                            # 종료값 : 9
                            # 증감값 : 1
    
    print(f'i의 값 : {i}')
print()                     # 빈 줄 삽입

for i in range(1, 11):      #
                            # 초기값 : 1
                            # 종료값 : 10
                            # 증감값 : 1
    print(f'i의 값 : {i}')
print()

for i in range(1, 11, 2):   # 홀수만 입력
                            # 초기값 : 1
                            # 종료값 : 10
                            # 증감값 : 2
    print(f'i의 값 : {i}')
print()

for i in range(10, 0, -1):  # 10부터 1까지 1감소
    print(f'i의 값 : {i}')
print()


for i in reversed(range(10)):   # reversed : 반전 9 - 0
    print(f'i의 값 : {i}')
print()


# 2. 비시퀀스 자료형 : 순서를 가지고 있지 않은 자료형
# 세트 ,딕셔너리


## 기본형식 ##
# 1. 세트
# for 요소 in {세트}:
#   반복실행

for item in {'가위', '바위', '보'}:
    print(item)

# 2. 딕녀너리 (dictionary)
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용을 함.
print()

person = {'name':'에밀리', 'age':20, '주소':'대구'}
for item in person:
    print(item)
print()


# value 출력

for key, value in person.items():       # 이걸 추천
    print(f'{key} : {value}')
print()

for key in person:
    print(f'{person[key]}')