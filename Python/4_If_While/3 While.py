### 반복문 ###
## while문 ##
# 특정조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용.


# 3 in 1 (Set) #
# 1. 탈출용 변수
# 2. 탈출용 조건식
# 3. 탈출용 증감식


num = 1             # 탈출용 변수
while num <= 10:    # 탈출용 조건식
    print('HELLO WORLD', end='')
    num += 1        # 탈출용 증감식
print('while문 Escape')


n = 1
while n <= 10:
    print(n)
    n += 1

print(f'탈출 후의 n의 값 : {n}')



## while문 중첩 ##
# while문 내부에 또 다른 while문이 나타나는 것


day = 1
while day <= 5:
    hour = 1
    while hour <= 3:
        print(f'{day}일차 {hour}교시 입니다.')
        hour += 1
    day += 1


## 무한 루프 - while 문 ##
while True:         # 무한 루프(반복), 숫자 1도 가능
# while 1:
    print('ㅋ', end='') # ㅋ 출력 후 Enter를 치지 않겠다
