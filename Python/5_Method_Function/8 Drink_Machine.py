# 700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지
# 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

# 함수 정의
# *반환값 : 없음
# 함수 이름 : vendingmachine()
# 매개변수 : 정수 money



# 실행 예)
# 음료수 = 0개, 잔돈 = 3000원
# 음료수 = 1개, 잔돈 = 2300원
# 음료수 = 2개, 잔돈 = 1600원
# 음료수 = 3개, 잔돈 = 900원
# 음료수 = 4개, 잔돈 = 200원

def vending_machine(money):
    drink_price = 700
    drink_count = 0
    drink_change = money
    count = money / drink_price
    
    while True:
        if drink_count > count:
            break
        else:
            drink_change = money - (drink_count) * drink_price
            print(f'음료수 = {drink_count}개, 잔돈 = {drink_change}원')
            drink_count += 1
            
    # while True:
    #     if drink_change > drink_price:
    #         drink_change = money - (drink_count) * drink_price
    #         print(f'음료수 = {drink_count}개, 잔돈 = {drink_change}원')
    #         drink_count += 1
    #     else:
    #         break
        
    return 
    
    # or 
    
    # cnt = money // drink_price
    # for x in range(cnt + 1):
    #     drink_change = money - (drink_count) * drink_price
    #     print(f'음료수 = {drink_count}개, 잔돈 = {drink_change}원')
    #     if x == cnt:
    #         return
    #     drink_count += 1
    
# 코드 최적화
# def vending_machine(money):
#     # 음료 가격
#     price = 700
    
#     # 반복 횟수
#     count = money // price    
#     for cnt in range(count + 1):
#         # 잔돈
#         change = money - cnt * price
#         print(f'음료수 = {cnt}개, 잔돈 = {change}원')

vending_machine(3000)