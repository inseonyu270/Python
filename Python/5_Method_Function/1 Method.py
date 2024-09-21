### 메서드 (메소드 == METHOD) ###
# 메서드 method란? : 특정 객체 Object가 가지고 이슨ㄴ 함수 Functions을 의미
# 함수는 독립적으로 호출할 수 있지만, 메서드는 트정 객체를 통해서만 호출이 가능하다


# 함수와 다르게 메서드는 특정 객체 소속이여서, 메서드를 호출하려면
# 트정 객체를 통해서만 호출 가능

# 1. 문자열 메서드
# 문자열 str를 처리하기 위해 많은 메서드를 제공

# 1) format()
print('안녕하세요 제 이름은 {}입니다.'.format('inseon'))


# 2 count()
# 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메서드

print()
s = "내가 그린 기린 그림은 목 긴 기린 그림이고, 내가 그린 기린 그림은 목 짧은 기린 그림이다."
print(s.count('기린'))


# 인덱스를 지정해 범위를 지정할 수도 있다.
s = 'best of best'
print(s.count('best', -7))      # 1

# 마이너스 인덱스도 가능


# 3) find()
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# 찾고자 하는 문자열이 있으면 그 문자열이 처음으로 나온 위치 즉 인덱스 index를 반환
print()

s = 'apple'
print(s.find('ap'))

# 찾는 문자열이 없는 경우 -1 반환
print(s.find('z'))


# 인덱스를 이용해서 검색할 범위도 지정 가능
# 시작할 인덱스를 지정하지 않은 경우에는 문자열의 처음부터 찾고, 시작할 인덱스를 지정하는 경우 지정된
# 인덱스부터 찾음.

s = 'best of bset'
print(s.find('best'))
print(s.find('best', 5))        # 시작 인덱스


# 4) index()
# find() 메서드와 같음. 사용방법도 같음. 차이점은 문자열이 없을 때 오류 발생
# find메서드는 찾는 문자열이 없는 경우 -1을 반환, index() 메서드는 오류 발생
s = 'apple'
print(s.index('z'))


# 5) 대소문자 변환 메서드
# upper : 모두 대문자로 변환
# lower : 모두 소문자로 변환
# capitalize : 첫 글자는 대문자로 변환, 나머지는 소문자로 변환

print()

s = 'BEST of best'
print(s.uperr())
print(s.lower())
print(s.capitalize())