# Shop 클래스를 완성해라
# 떡볶이 : 3000원, 순대 : 3000원, 튀김 : 500원, 김밥 2000

# 현재 매출액 : 3000원
# 현재 매출액 : 7000원
# 현재 매출액 : 9500원
# 하루 총 매출 : 9500원


class Shop:
    shop_menu = {
        '떡볶이' : 3000,
        '순대' : 3000,
        '튀김' : 500,
        '김밥' : 2000
    }
    
    total = 0
    
    @classmethod
    def sales(cls, menu, count):
        sale_total = cls.shop_menu[menu] * count
        print(f'현재 매출 {sale_total}원')
        cls.total += sale_total        

# 풀이
# class Shop:
#     total = 0
#     @classmethod
#     def sales(cls, menu, amount):
#         if menu == '떡볶이' or menu == '순대':
#             cls.total += (3000 * amount)
#         if menu == '김밥':
#             cls.total += (2000 * amount)
#         if menu == '튀김':
#             cls.total += (500 * amount)
#         print(f'현재 매출액 : {cls.total}원')


Shop.sales('떡볶이', 1)     # 메뉴, 수
Shop.sales('김밥', 2)       # 메뉴, 수
Shop.sales('튀김', 5)       # 메뉴, 수
print(f'하루 총 매출 : {Shop.total}원')