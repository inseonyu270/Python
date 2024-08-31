# 5자리로 구성된 학번 '31025'를 학년
# 반, 번호로 나누어 출력하는 프로그램을 구현하세요

# 실행 예)
# 3학년 10반 25번

num = '31025'

# print(num[0:1]+'학년',num[1:3]+'반', num[3:5]+'번')

grade_no = num[0]
class_no = num[1:3]
number = num[3:]

# 3 학년 10 반 25 번
print(grade_no, "학년", class_no, "반", number, "번")
print(grade_no, "학년", class_no, "반", number, "번", sep='')

## print() Option ##
print(1, 2, 3)          # 1 2 3
print(1, 2, 3, sep='')  # 123       // sep : 값들의 사이사이 구분자를 어떻게 처리할껀지 지정
print(1, 2, 3, sep=':') # 1:2:3     // 출력 사이사이에 :(콜론)을 출력
print(1, 2, 3, sep=',') # 1,2,3     // 출력 사이사이에 ,(콤마)를 출력


print('Hello')
print('Python')                     # Hello 출력하고 줄바꿈이 실행되고 Python이 출력됨.

# Hello와 Python을 붙여서 출력하고 싶음
print('Hello', end='')              # end   : 마지막 줄바꿈을 어떻게 처리할껀지 지정
                                    # end='': 엔터 기능 대신 아무것도 넣지 않겠다.
print('Python', end='         ')    #       : 엔터 기능 대신 스페이스(공백)을 넣겠다
print('싫어')