### % 연산자 (Default Formatting) ###
# == 서식문자 == 형식있는 문자 == 자리가 있다.

name = 'Kai'
print('내 이름은 %s입니다.' %name)      # %s : string(문자열을 받는다)
print('내 이름은 ', name, '입니다', sep='')
print('내 이름은 ' + name + '입니다')

height = 120.6
print('내 키는 %fcm입니다.' %height)    # %f : float(실수형)


weight = 23.55
print('내 몸무게는 %.1fkg' %weight)     # %.1f : 소수점 첫째자리까지 출력


year, month, day = 2024, 7, 10

print('내 생일은 %d년 %d월 %d일 입니다.' %(year, month, day))   # %d : deciaml(10진 정수)
