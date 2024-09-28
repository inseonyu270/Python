import random
from datetime import *

# 1 ~ 100사이의 시스템이 만든 랜덤한 수 생성
number = random.randint(1, 100)




# 친절 문구 출력
print('updown 게임을 시작합니다.')

# 시작 전에 시작 시간 생성
start = datetime.now()          # 현재 시작 시간을 start변수에 저장

# 무한 루프 == 맞출 때까지 입력받겠다.

while True:
    
    
    # 사용자로부터 값을 입력받기
    user = int(input('어떤 값일까요?'))
    
    # 사용자 입력값과 시스템 값을 비교
    # 서로 일치
    if number == user:
        # 끝시간 생성
        end = datetime.now()    # 현재 끝난 시간을 end변수에 저장
        
        
        # 걸린 시간 == 끝 - 시작
        value = end - start     # 끝 - 시작 ==> 걸린 시간
        
        print (value)           # 0:00:05.983217
        value = value.total_seconds()   # 5.98217
                                        # end - start 코드에서 생긴 시간 간격을 초 단위 확산
        
        print(f'정답입니다. 걸린 시간 {value}')
        print('시스템을 종료합니다.')
        break
    
    # 서로 일치하지 않음
    else:
        # 일치하지 않다면 시스템 수와 유저 수의 비교
        # 유저수 > 시스템 수 ==> 다운
        if user > number:
            print('오답입니다 .다시 입력해주세요.')
            print('다운')
        # 유저수 < 시스템 수 ==> 업
        else:
            print('오답입니다. 다시 입력해주세요.')
            print('업')