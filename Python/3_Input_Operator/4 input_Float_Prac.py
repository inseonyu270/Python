# 사용자로부터 2개의 실수를 입력받아 합게를 구하는 프로그램을 구현하세요!!

# [출력값]
# 첫번째 실수를 입력하세요 >>> 3.12
# 두번째 실수를 입력하세요 >>> 2.11
# 두 실수의 합계는 : 5.23

num1 = float(input('첫번째 실수를 입력하세요 >>> '))
num2 = float(input('두번째 실수를 입력하세요 >>> '))

sum = num1 + num2

print(f'두 실수의 합계는 : {sum}')
#print('두 실수의 합계는 : ' + str(sum))
#print('두 실수의 합계는 : ', sum)
#print('두 실수의 합계는 : {}'.format(sum))
#print('두 실수의 합계는 : %.1f', %sum)
#print('두 실수의 합계는 : {p_sum}'.format{p_sum=sum})