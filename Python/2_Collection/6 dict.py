### 딕셔너리 (Disctionart) ###
# 사전처럼 어떤 단어와 그 단어의 의미로 구성
# '키(Key)'와 '값(Value)'을 '단어'와 '단어의 의미'처럼 사용
# 딕셔너리라는 인덱스가 존재하지 않는 대신 키를 인덱스처럼 사용함.
# 키 값을 알면 저장된 값을 확인할 수 있는 구조


# 키:값 == 한 쌍

d = {'a': 'apple', 'b':'banana'}        # {key:value, ket:value}

print(d)
print(type(d))
print(d['a'])
print(d['b'])

# 키 값의 자료형이 문자열(str) 이라면 (dict) 메서드를 이용해서 생성 가능
d = dict(a='apple', b='banana')
print(d)



## 딕셔너리 요소와 추가와 삭제 ##
## 새로운 키와 값을 조합해서 작성 ##
print()
dic = {'apple':'사과'}
dic['apple'] = '바나나'     # 딕셔너리 값을 수정할 때
dic['watermelon'] = '멜론'  # 딕셔너리 쌍을 추가할 때
                            #결론 : 딕셔너리에 키가 없다면 '추가', 키가 있다면 값을 '변경(수정)
print(dic)

# 존재하는 키값을 이용해서 정의하면, value 수정으로 인식
dic['watermelon'] = '수박'
print(dic)

# setdefault() 메서드를 이용해서 추가
me = {'name':'james'}
me.setdefault('age',20)
print(me)

# update() 메서드를 이용해 존재하는 키값이면 수정
me.update(age=25)
print(me)

# update() 메서드의 경우 존재하지 않는 키값이면 추가
me.update(address='서울')

# 딕셔너리 삭제(del)
del me['address']       # address : 서울 삭제
print('딕셔너리', me)

# keys() 메서드     : 키(Key)만 모아 출력
print(me.keys())

# valuse() 메서드   : 값(Value)만 모아 출력
print(me.values())

# items 메서드      : 딕셔너리 쌍을 튜플로 묶어 출력
print(me.items())

# clear 메서드      : 모든 Key:Value 삭제
me.clear()
print(me)