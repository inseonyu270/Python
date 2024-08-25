
# 문자열 인덱싱

'''
[문제]
출력결과를 참고하여 문자열 인덱싱으로 할글자씩 출력해보자

string = 'PYTHON'

[출력결과]
P
Y
N
N
H

'''

string = 'PYTHON'

#슬라이싱
print(string[0:1:1])    # P
print(string[1:2:1])    # Y
print(string[5::1])     # N
print(string[5::1])     # N
print(string[3:4:1])    # H

# 인덱싱
print(string[0])
print(string[1])
print(string[5])
print(string[-1])    
print(string[3])