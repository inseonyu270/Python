# 논리 연산자
# 결과 값은 True 외 False 둘 중 하나
# a and b : a와 b가 모두 참 ( True )이면 True, 아니면 False
# AND : 왼쪽 항이 True여도 오른쪽 항을 True, False 확인
#     : 왹쪽 항이 False라면 오른쪽 항 연산 X ==> 무조건 False 


# a or b : a와 b중 하나라도 참( True )이면 True, 아니면 False 
# OR : 왼쪽 항이 True라면 오른쪽 항을 연산 X ==> 무조권 True
#    : 왼쪽 항이 False라면 오른쪽 항을 True, False 확인


# not a : a가 참( False ), 거짓 ( True )

a = 10
b = 0

print(f'{a} > 0 and {b} > 0 : {a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}')
print(f'not {a} : {a, not a}')
print(f'not {b} : {b, not b}')