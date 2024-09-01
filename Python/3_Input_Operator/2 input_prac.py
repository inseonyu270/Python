# 이름과 나이를 물어보고 이름과 나이를 출력하는 프로그램을 구현

# [출력값]
# 이름을 입력하세요 >>> 홍길동
# 나이를 입력하세요 >>> 20
# 입력된 이름은 홍길동입니다.
# 입력된 나이는 20살입니다.

name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')

# f-strings
print(f'입력된 이름은 {name}입니다.')
print(f'입력된 나이는 {age}살입니다.')

# format
#print('입력된 이름은 {}입니다.'.format(name))                  // 형식 지정자 {}
#print('입력된 나이는 {}입니다.'.format(age))

#print('입력된 이름은 {f_name}입니다.'.format(f_name=name))     // 변수 활용
#print('입력된 나이는 {f-age}입니다.'.format(f_age))            

# %연산자
#print('입력된 이름은 %s입니다.' %name)
#print('입력된 나이는 %d입니다.' %age)    

# print() sep옵션
#print('입력된 이름은 ', name, '입니다.', sep='')
#print('입력된 나이는 ', age, '입니다.', sep='')
