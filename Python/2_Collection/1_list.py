
### Collection (컬렉션) Like 자료구조 ###

### 리스트 ( List ) ###
# 여러 값을 저장할 때 가장 많이 사용하는 자료형
# 저장하고자 하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장

# 대괄호([]) 또는 list() 함수를 이용해서 생성
# 정수, 실수, 문자열을 각 1개씩 저장하고 있는 리스트 생성

li = [100, 3.14, 'Hello']
print(li)
print(type(li))

## 인덱싱 ( Indexing ) ##
# 문자열과 동일한 방식으로 인덱싱을 지원
# 저장된 요소들마다 고유번호인 인덱스를 부여하여 순서대로 관리

print()
print(li[0])
print(li[1])    
print(li[2])

## 슬라이싱 ( Slicing ) ##
print()
li = [10, 20, 30, 40]

print(li[0:3])
print(li[0:2])
print(li[::3])


## 요소의 추가와 삭제 ##
## 추가 ##
# 새로운 요소를 추가할때는 append(), insert() 메서드 사용
# append() 항상 마지막 요소로 추가
# insert() 추가할 인덱스(위치 정보)를 지정
print()


scores = [50, 40, 30]
scores.append(100)      # 마지막 요소에 100을 추가
                        # list 가지고 있는 append()를 사용하겠다.
                        # . (~안에)

print(scores)           # 현재 list의 상태 : [50, 40, 30, 100]
print(scores[3])        # 100
scores.insert(1, 30)    # 현재 list의 상태 : [50, 30, 40, 30, 100]
print(scores)


## 삭제 ## 이승기 삭제
# pop() : 인덱스를 전달하지 않으면 마지막 요소를 삭제
# 인덱스를 전달하면 인덱스의 요소를 삭제
print()
scores.pop()            #마지막 요소 삭제
print(scores)
scores.pop(1)           # 1번 인덱스 요소를 삭제
print(scores)

scores[0] = 60          # 0번째 index 자리에 60을 넣겠다(50은 삭제가 되고, 60이 삽입)
print(scores)


# del           : 키워드(예악어)
# 형식 #
# del list_name[Index_number]
print()
del scores[1]
print(scores)

# 슬라이싱을 위해 값 추가
scores.append(100)
scores.append(110)
scores.append(120)
scores.append(130)
scores.append(140)
print(scores)

del scores[0:3]
print(scores)
