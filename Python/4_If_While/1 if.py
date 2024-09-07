### 조건문 ###
## if문 ##

# 1. if문의 형식
# if 조건식 : 
#   조건식의 결과가 True일때 실행할 코드를 적는 섹션(Section)


num = 15
if num > 0:
    print('if문 진입')
    print('양수')       # 조건식이 True라서 실행됨.
print('if문 종료한 후 실행되는 코드입니다.')


if True:
    print('참')

if False:
    print('틀렸다')


# 들여쓰기 ( identation ) 규칙 #
# 1. 공백(space)나 탭(Tab)을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관 X
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 한다.
#   공백과 탭을 혼용해서 사용할 수 없고, 들여쓰기 수준도 통일해야 한다.
# 5. 주로 사용하는 들여쓰기는 공백 4개, 공백 1개, 탭 1개

if num > 0: print('양수')       # 실행문이 하나면 한줄 코드도 가능

# 2. if-else문의 형식

number = int(input('짝/홀수 구분해줄게 수 입력해봐 >>> '))
if number %2 == 0:
    print('2의 배수다')
else:
    print('2의 배수가 아니다.')


# 3. if-elseif문의 형식
# if 조건식1 :
#      조건식 1의 결과가 true일 때 실행
# elif 조건식2 :
#      조건식 1의 결과가 False이고, 조건식2의 결과가 True일 때 실행
# elif 조건식3 :
#      조건식 1의 결과가 False이고, 조건식2의 결과가 False이고, 조건식3의 결과가 True면 실행
# else:
#      조건식 1, 2, 3의 결과가 모두 False이면 실행

age = 13        
if age >= 20:       # 20살 이상
    print('성인입니다.')
elif age >= 8:      # 20살 미안 8살 이상
    print('학생입니다.')
else:
    print('응애')
print()
