### 튜플 (Tuple) ###
# 저장된 값을 변경할 수 없는 리스트
# 리스트와 마찬가지로 각 요소를 구분하기 위한 인덱스가 부여되고 슬라이싱도 지원
# 이미 저장된 값 이외에는 추가, 수정, 삭제가 불가능

# 튜플은 소괄호()나 tuple() 함수를 이용해서 생성
# 값들을 콤마(,)로 분리하여 전달하면 자동으로 튜플이 생성

t1 = (1, 2, 3)
print(t1)


t2 = 1, 2, 3
print(t2)

t3 = tuple([100,3.14, 'hello'])
print(t3)


# 값을 1개만 보관하는 튜플을 생성할 경우에는 값과 콤마(,)를 반드시 함께 작성
t4 = (100)
print(t4)
print(type(t4))

t5 = (100, )
print(t5)

a = 10
b = 20

print(a, b)
a, b = b, a
print(a, b)
