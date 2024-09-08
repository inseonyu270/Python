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