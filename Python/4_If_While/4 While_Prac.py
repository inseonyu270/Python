# 1부터 10까지 합을 구해 출력하기
# 출력예)
# 1부터 10까지의 합의 결과 : 55

num = 1
sum = 0

while num <= 10:
    sum += num
    num += 1
print(f'{sum}')

# 1부터 N(입력받은 수)까지 합을 구해 출력하기

n = int(input('수 입력 :'))
num = 1
sum = 0

while num <= n:
    sum += num
    num += 1
print(f'{sum}')


# n부터 m까지 합을 구해 출력하기
# 제약조건(Constraint) : n이 '''무저건''' m보다 작은 경우로 처리해라 

n = int(input('n : '))
m = int(input('m : '))
sum = 0
n_re = n
m_re = m

if n < m:
    while n_re <= m:
        sum += n_re 
        n_re += 1
    print(f'{n} 부터 {m}까지의 합 : {sum}')
elif n < m:
    while m_re <= n:
        sum += m_re
        m_re += 1
    print(f'{m}부터 {n}까지의 합 : {sum}')
else:
    print(f"{n}과 {m}은 같음")

# 구구단 2단 출력하기
n = 1
num = 0

while n < 10:
    print(f'2 X {n} = {2 * n}')
    n += 1



# # 100부터 50 사이의 짝수를 출력
num = 100

while num >= 50:
    if num % 2 == 0:
        print(f'{num}')
    num -= 1


# 1부터 N(입력받은 수)까지 짝수의 합과 홀수의 합을 나누어 저장하고 출력
n = int(input('N : '))
num = 1
even = 0
odd = 0

while num <= n:
    if num % 2 == 0:        # 짝수
        even += num
    elif num % 3 == 0:      # 홀수
        odd += num
    num += 1

print(f'1부터 {num}까지 짝수의 합 : {even}')
print(f'1부터 {num}까지 홀수의 합 : {odd}')


# 사용자로부터 임의의 정수를 입력받아 모두 리스트에 보관
# 단 사용자가 0을 입력하면 프로그램을 종료. 이때 받은 0은 리스트에 보관하지 않음

number = []
while 1:
    num = int(input('숫자 입력 : ')) 
    if num == 0:
        break
    number.append(num)
print(f'입력된 정수 리스트 : {number}')


# 구구단 2단 부터 9단까지 출력
# 각 단 앞에 제목, 마지막에 구분선을 넣어볼 것
dan = 2
num = 1
while dan <= 9:
    print(f'------------{dan}단---------------')
    while num <= 9:
        print(f'{dan} X {num} = {dan * num}')
        num += 1
    dan += 1
    num = 1
print('--------------------------------')



# 임의의 정수를 입력받아 정수가 입력되면 ex) : 3 -> 5단 출력
dan = int(input('dan : '))
num = 1

while 3 <= dan:
    print(f'{dan} X {num} = {dan * num}')
    num += 1
print('---------------------------------------')



# 커피 1잔을 300원에 판매하는 커피자판기가 있습니다.
# 이 커피자판기에 돈을 넣으면 자판기에서 뽑을 수 있는 커피가 몇 잔이며
# 잔돈은 얼마인지를 함께 출력하는 프로그램을 구현하세요.
price = int(input('돈 : '))
coffee = 300

    
if price <= 0:
    print('금액은 0원 이상의 정수여야 합니다.')
else:
    count = 0
    while price >= 300:
        count += 1
        price -= coffee
    print(f'커피 구매 갯수 : {count} 잔돈 : {price}')