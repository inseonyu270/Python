# 커피 자판기 프로그램
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# '아메리카노' : 1000,
# '카페라떼' : 1500,
# '카푸치노' : 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환        잔돈 : ???원, 커피 없는 메뉴
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환           잔돈 : ???원, 커피 금액부족
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환                잔돈 : ???원, 커피 아메리카노


def coffee_machine(money, pick):
    print(f'[SYSTEM] : {money}원에 {pick}을 선택하셨습니다.')
    print()
    
    coffee_list = {
        '아메리카노' : 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    
    # 비정상 주문 (돈 O, 메뉴 X)
    if pick not in coffee_list:
        print(f'[SYSTEM] : {pick}는 없는 메뉴입니다. 죄송합니다.')
        return money, '없는 메뉴'
    
    # 비정상 주문 (돈 X, 메뉴 O)
    elif coffee_list[pick] > money:
        print(f'[SYSTEM] : 금액이 부족합니다, {pick}은 {coffee_list[pick]}원 입니다.')
        return money, '금액부족'
    
    # 정상 주문 (돈 O, 메뉴 O)
    else:
        return money - coffee_list[pick], pick

order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ')

pay = int(input(f'{order}를 선택하셨습니다. 얼마 결제하시겠습니까?'))
print()

change, coffee = coffee_machine(pay, order)

print(f'잔돈 {change}원, 커피 {coffee}')