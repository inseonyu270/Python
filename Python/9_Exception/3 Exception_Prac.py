# 문제

# 한 가게에서 고객의 주문을 처리하는 프로그램을 작성하려 한다.
# 사용자로부터 주문한 제품의 가격과 수량을 입력 받아서 총 주문 가격을 계산하는 프로그램을 작성하려고 한다.
# 그러나 다음과 같은 상황들은 예외 처리해야한다.

# 1. 가격과 수량을 입력할 때 숫자가 아닌 값이 입력되면 "올바른 숫자를 입력하세요" 라는 메시지가 나와야 한다.
# 2. 가격이 음수인 경우 "가격은 음수일 수 없습니다."라는 메시지가 나와야 한다.
# 3. 수량이 음수인 경우 "수량은 음수일 수 없습니다." 라는 메시지가 나와야 한다.

try:
    price = int(input('가격 : '))
    count = int(input('수량 : '))
    
    if price < 0:
        raise Exception('가격은 음수일 수 없습니다.')       
    if count < 0:
        raise Exception('수량은 음수일 수 없습니다.')
    
except ValueError:
    print('올바른 숫자를 입력하세요.')
except Exception as a:
    print(a)

# or

# try:
#     price = int(input('가격 : '))
#     count = int(input('수량 : '))
    
#     if price < 0:
#         raise ValueError('가격은 음수일 수 없습니다.')       
#     if count < 0:
#         raise ValueError('수량은 음수일 수 없습니다.')
    
# except ValueError as e:
#     print(e)
# except Exception as a:
#     print('오류 발생', a)

# raise : 예외를 명시적으로 발생시킬 수 있다
# 예외를 발생시켜 코드의 흐름을 제어하거나 오류를 처리 할 수 있음.
# 형식 : raise 예외이름(예외메세지)