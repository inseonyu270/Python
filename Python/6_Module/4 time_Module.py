### time 모듈 ###
import time


# 1) time() 함수
# 1970년 1월 1일 0시 0분 0초부터 현재까지 경과된 시간 timestamp를 반환
# 소주점 이하는 마이크로 초를 의미
print(time.time())

# 2) ctime() 함수
# 인수로 전달된 시간 timestamp 형식에 갖춰 반환
print(time.ctime(time.time()))

# 3) sleep() 함수
# 인수로 전달된 초 second 만큼 시스템을 일시 정지
time.sleep(5)

print('5초 뒤에 뜸')

# 4) datetime 모듈
# 날짜와 시간 데이터를 처리할 때 사용
print()
import datetime

# 1. now() 메서드
# datetime 모듈 내부에 정의된 메서드
# 시스템의 현재나 ㄹ짜와 시간을 반환 
now = datetime.datetime.now()       # 모듈 datetime.클래스 datetime.메서드 now()
print(now)

# 2. date() 함수
# 특정날짜를 반환
birthday = datetime.datetime(2014, 1, 29, 12, 12, 12)
print(birthday)