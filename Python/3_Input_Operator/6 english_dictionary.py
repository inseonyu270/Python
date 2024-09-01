# 파이썬으로 영어사전을 구현하고자 한다.
# 다음과 같은 딕셔너리 (dict)을 하나 생성하고 실행 예와 같이 동작하는 프로그램을구현하세요.

### 사전 내용 ###
# flower = 꽃
# fly == 날다
# floor == 바닥

# 출력 예)
# 영어 단어를 입력하세요 >>> flower
# flower : 꽃

eng_dict = {
    'flower':'꽃',
    'fly':'날다',
    'floor':'바닥'
    }
eng = input('영어 단어를 입력하세요 >>> ')

print(f'{eng} : {eng_dict[eng]}')