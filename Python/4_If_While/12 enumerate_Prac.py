# 문제 : 출력결과를 보고, enumerate를 사용해서 출력하시오.
# 1월 = 31
# 2월 = 28
# 3월 = 31
# 4월 = 30
# 5월 = 31
# 6월 = 30
# 7월 = 31
# 8월 = 31
# 9월 = 30
# 10월 = 31
# 11월 = 30
# 12월 = 31

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(days):
    print(f'{month + 1}월 = day')