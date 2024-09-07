# 1. 나이를 입력받아 20살 이상이면 '성인', 20살 미만이면 '미성년자'를 출력하는 프로그램입니다.

age = int(input('나이 입력 : '))

if age >= 20:
    print('성인')
else:
    print('미성년자')

# 2. 나이를 입력받아 7살 이하면 '미취학', 8~13이면 '초등학생', 14~16살이면 '중학생',
# 17~19살이면 '고등학생', 20살 이상이면 '성인'을 출력하는 프로그램입니다.

age = int(input('나이 : '))

if age <= 7:
    print('미취학')
elif age <= 13:
    print('초등학생')
elif age <= 16 :
    print('중학생')
elif age <= 19: 
    print('고등학생')
else:
    print('성인')

# 3. 
# 점수를 입력받아서 학점을 출력하는 프로그램을 구현하세요.
# 학점은 점수가 100~90점 이면 'A',
#              89~80점 이면 'B',
#              79~70점 이면 'C',
#              69~60점 이면 'D',
#              59~0점 이면 'F'입니다

score = int(input('점수 : '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 임의의 정수를 입력받은 뒤 해당 값이 3의 배수인지 아닌지 판별하는 프로그램을 구현하세요
# 실행 예)
# 정수를 입력하세요 >>> 14
# 14는 3의 배수가 아닙니다.

num = int(input('정수 입력 :'))

if num % 3 == 0:
    print(f'{num}은 3의 배수입니다.')
else:
    print(f'{num}은 3의 배수가 아닙니다.')