### 복합대입 연산자 ###
# 복합대입 연산자 == 산술 연산자 + 대입 연산자

piggy_bank = 1000

money = 10000

# piggy_bank = piggy_bank + money
piggy_bank += money
print(f'저금통에 돈{money}원을 넣었습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')

snack = 2000

piggy_bank -= snack     # piggy_bank = piggy_bank - snack
print(f'저금통에서 스낵 구입비 {snack}원을 뺐습니다.')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다.')