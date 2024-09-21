### 시퀀스 내장 함수 ###


# len() : 함수에 전달된 객체의 길이 (항목 수)를 반환
print()

li = ['a', 'b', 'c', 'd']
print(len(li))

a = {'a' : 'apple', 'b' : 'banana'}
print(len(a))       # 2   - 딕셔너리는 키 : 값으로 구성된 한 쌍을 하나의 데이토로 본다

print(len(range(10)))
print(len(range(1, 10)))


# range() 함수와 리스트의 길이를 구하는 len() 함수를 함께 사용하면 리스트의 인덱스를 생성 가능

seasons = ['봄', '여름', '가을', '겨울']
seasons_eng = ['spring', 'summer', 'fall', 'winter']

len(seasons)            # 봄, 여름, 가을, 겨울을 가지는 seasons라는 리스트의 길이 = 4
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')


# sorted() : 전달된 반복가능객체의 오름차순 정렬 결과를 반환
# reverse = True : 옵션을 추가할 경우 내림차순 정렬 결과를 반환

print()
my_list2 = ['b', 'c', 'a', 'd']
print(sorted(my_list2))

my_list = [6, 3, 1, 2, 5, 4]
print(sorted(my_list))
print(sorted(my_list, reverse=True))


# zip() : 전달된 여러 개의 반복가능객체의 요소를 튜플로 묶어서 반환
# 전달된 반복가능객체들의 길이가 서로 다르면 짧은 반복가능객체 기준으로 동작
print()


names = ['james', 'emily', 'amanda']
scores = [60, 70 ,80]
for student in zip(names, scores):
    print(student)
    
# 튜플은 언패킹이 가능하다. 그래서 다음과 같은 모습으로 구성 가능
# 튜플 언패킹(Tuple Unpacking) : 튜플로 구성되어 있는 퓨틀 형태를 여러 개의 변수에 할당할 수 있음.
#EX)
t1 = (1, 2, 3)

# 튜플을 이용한 변수 할당
a, b, c = t1
print(a, b, c)

for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}입니다.')
    
for a, b in zip(seasons, seasons_eng):
    print(f'{a}의 계절은 {b}입니다.')
    

# enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스를 튜플 형태로 함께 추출
# for in enumerate([리스트]):
#      반복실행문

for item in enumerate(['가위', '바위', '보']):
    print(item)
    
for idx, element in enumerate(['가위', '바위', '보']):
    print(idx, '/', element)
    