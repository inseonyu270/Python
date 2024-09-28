# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 맞히는 프로그램입니다.
# 사용자가 맞힐 때까지 게임은 계속됩니다.
import random
from datetime import *

print('--------------- 주사위 게임 ---------------')
num = random.randint(1, 6)
# start time
st = datetime.now()

while True:
    user = int(input('숫자 : '))
    # True
    if user == num:
        # end time
        end = datetime.now()
        time = end - st
        time = time.total_seconds()
        
        print(f'정답 \n걸린시간 : {time}')
        print('게임 종료')
        break
    # False
    else:
        print('오답')