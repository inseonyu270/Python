# 가방을 만들 때마다 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스

# 출력예) #
# 현재 가방 0
# 현재 가방 3
# 현재 가방 1

class Bag:
    total_bag = 0
    
    def __init__(self):
        Bag.total_bag += 1
    
    @classmethod
    def sell(cls):
        cls.total_bag -= 1
    
    @classmethod
    def remain_bag(cls):
        return cls.total_bag





print(f'현재 가방 {Bag.remain_bag()}')
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 {Bag.remain_bag()}')
bag1.sell()
bag2.sell()
print(f'현재 가방 {Bag.remain_bag()}')


