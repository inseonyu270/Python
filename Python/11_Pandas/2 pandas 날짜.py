import pandas as pd

# 인덱스 범위 지정만이 목적
# 시작 날짜와 끝 날짜를 지정해 데이터를 생성. 하루씩 증가한 날짜 데이터가 생성된다.
# print(pd.date_range(start='2024-10-23', end='2024-10-26'))

# 날짜 데이터를 입력할 때 yyyy-mm-dd 형식이 아니라
# yyyy/mm/dd, yyyy.mm.dd, mm-dd, yyyy, mm/dd/yyyy, mm.dd.yyyy  같은 형식도 사용 가능
# 대신 출력은 yyyy-mm-dd 형식으로 실행
# print(pd.date_range(start='2024/01/01', end='2024.1.13'))

# 끝 날짜를 지정하지 않고 periods만 입력해서 날짜 생성
# print(pd.date_range(start='01-01-2024', periods=7))     # 얼마만큼 날짜를 추가하겠다.


# 약어      설명        사용 예
# D         달력        날짜 기준 하루 주기 ex) 하루 주기 : freq = 'D' 이틀주기 : freq = '2D'
# B         업무        날짜 기준 하루 주기 ex) 업무일(월~금) 기준으로 생성


# 2일씩 증가하는 날짜를 생성

# print(pd.date_range(start='2024-01-01', periods=4, freq='2D'))

# 달력의 요일을 기준으로 일주일 씩 증가하는 날짜를 생성
# print(pd.date_range(start='2024-01-01', periods=12, freq='B'))


# 분기 시작일을 기준으로 4개의 날짜를 생성
# print(pd.date_range(start='2024-01-01', periods=4, freq='QS'))


# 연도의 첫날을 기준으로 1년 주기의 3개의 날짜 생성
# print(pd.date_range(start='2024-01-01', periods=3, freq='AS'))


# 날짜뿐 아니라 시간을 생성

# 1시간 주기로 10개의 시간을 생성
# print(pd.date_range(start='2024-01-01 08:00', periods=10, freq='H'))


# 30분 단위로 4개의 시간을 생성

# 30min으로 설정해도 출력은 30T
# print(pd.date_range(start='2024-01-01 08:00', periods=4, freq='30min'))


# S = 초, 10S = 10초마다 출력
# print(pd.date_range(start='2024-01-01 10:00', periods=5, freq='10S'))



# 문제 : date_range() 함수를 사용하여 
# 2024년 1월 1일부터 2024년 12월 31일까지의 인덱스를 갖는 데이터 프레임을 생성하시오.
import pandas as pd

date_range = pd.date_range(start='2024-12-31', end='2024-12-31')


df = pd.DataFrame(index=date_range)

print(df)


# 문제 1: 날짜와 랜덤 데이터 생성
# date_range() 함수를 사용하여 2024년 1월 1일부터 2024년 1월 31일까지의 날짜를 인덱스로 하고, 
# 각 날짜에 대한 랜덤한 온도(예: -10도에서 30도 사이의 값)를 생성한 후 데이터 프레임을 만드세요.
import pandas as pd
import numpy as np

# 날짜 범위(index) 생성
date_range = pd.date_range(start="2024-01-01", end="2024-01-31")
# print(date_range)

# 랜덤 온도 데이터(values) 생성 (-10도에서 30도 사이)
temperatures = np.random.randint(-10, 30, size=len(date_range))

# 데이터 프레임 생성
df = pd.DataFrame(temperatures, index=date_range, columns=['Temperature'])
print(df)

# 문제 2: 데이터 프레임의 기초 통계만
# 문제 1에서 생성한 데이터 프레임에 대해 다음 통계를 계산하세요:

# # 평균 온도
# mean_temp = df['Temperature'].mean()

# # 표준편차
# std_temp = df['Temperature'].std()

# # 최댓값
# max_temp = df['Temperature'].max()

# # 최솟값
# min_temp = df['Temperature'].min()

# print(f'평균 온도 : {mean_temp:.2f}도')
# print(f'온도의 표준편차 : {std_temp:.2f}도')
# print(f'최댓값 : {max_temp}도')
# print(f'최솟값 : {min_temp}도')

# print(df.describe())


# 문제 3
# 문제 1에서 생성한 데이터 프레임에서 2024년 1월 15일의 온도 데이터 출력하세요.
temp_jan_15 = df.loc['2024-01-15']
print(f'2024년 1월 15일의 온도 : {temp_jan_15['Temperature']}도')



# 문제 4
# 문제 1에서 생성한 데이터 프레임에 각 날짜의 요일 추가해서 새로운 열 추가(예 : 월,화,수,목,금 등)

df['Weekday'] = df.index.day_name()
print(df)

# 문제 5
# 문제 1에서 생성한 데이터 프레임의 온도 변화를 시각화하기

# pip install matplotlib
import matplotlib.pyplot as plt

# 그래프 크기 설정
plt.figure(figsize=(10, 5))         # 10 : 너비 , 5 : 높이


# 데이터 플로팅
plt.plot(df.index, df['Temperature'], marker='o')      # df.index : x축에 사용할 데이터, 날짜 인덱스를 사용함.
                                                       # df['Temperature'] : y축에 사용할 테이터, 온도 열을 사용함.


# 그래프 제목 설정
plt.title('2024-01 Temperature')

# x축  레이블과 y축 레이블 설정
plt.xlabel('DATETIME')
plt.ylabel('TERMPERATURE(°C)') 


# x축 눈금 회전 
plt.xticks(rotation=45)

plt.grid()



plt.show()