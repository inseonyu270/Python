# 문제
# while True: ==> 무한 반복을 이용해서 푸는 문제
# 대한민국 수도가 어디인지 물어보고 서울, seoul, SEOUL 만 정답, 나머진 오답
# 맞출때까지 물어보세요 

# 정답시 
# 대한민국 수도는 어디인가요 >>> 서울
# 정답입니다.


# OR
# 오답시 
# 대한민국 수도는 어디인가요 >>> 부산
# 오답입니다. 다시 시도하세요
# 대한민국 수도는 어디인가요 >>> seoul
# 정답입니다.

#정답시 대한민국 수도는 어디인가요 >>> SEOUL

while True:
    korea = input("대한민국 수도는 어디인가요 >>> ")
    
    if korea == '서울':
        print('정답입니다.')
        break
    if korea == 'seoul':
        print('정답입니다.')
        break
    if korea == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다.')


# OR

while True:
    city = input("대한민국 수도는 어디인가요 >>> ")
    
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다.')