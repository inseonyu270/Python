# 오늘의 스케줄을 입력하면 그 내용이 모두 파일에 보관되는 프로그램이다.
# 스케줄을 입력하지 않고 enter 누르면 프로그램은 종료됩니다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-02-01.txt'와 같은 형식을 갖추고 있습니다.

# 참고 : 오늘은 2월 1일이지만 내일 실행할 때는 2월 2일이 찍히도록 해야한다.

# hint : time 모듈을 불러오세요
# ++) time.strftime()을 구글링해서 사용해보세요


# time.strftime()
# 정의 : strf == string format time의 약어
# 기능 : 시간 및 날짜 정보를 특정 문자열로 변환(포맷팅)하는데 유용함.
# 형식 지정자
# %Y : 4자리 연도 (예 : 2004)
# %y : 2자리 연도 (예 : 24)

# %m : 2자리 월 (01 ~ 12)
# %d : 2자리 일 (01 ~ 31)

# %H : 24시간 형식의 시간 (00 ~ 23)
# %I : 12시간 형식의 시간 (01 ~ 12)
# %M : 2자리 분 (00 ~ 59)
# %S : 2자리 초 (00 ~ 59)
# etc...

import datetime
from time import strftime

time = datetime.datetime.now()
txt_time = time.strftime("%Y-%m-%d")

file = open(f'./9_Exception/Schedule/{txt_time}.txt', 'at', encoding='utf-8')

print('(아무것도 없는 상태에서 enter를 칠 시 종료)')

while True:
    schedule = input('스케줄 입력 : ')
    if not schedule:
        break
    file.write(schedule + '\n')
    