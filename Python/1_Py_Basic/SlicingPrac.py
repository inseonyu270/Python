
# 문자열 슬라이싱
'''
[문제]
문자열 슬라이싱으로 출력결과와 같도록 출력해보자.

mystr = 'GOOD NIGHT'

[출력결과]
OO
 NIGHT
GH
OD
'''

mystr = 'GOOD NIGHT'

print(mystr[1:3:])     # OO
print(mystr[4::])       #  NIGHT
print(mystr[0::8])      # GH
print(mystr[2:4:])     # OD