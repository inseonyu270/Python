# 2. 리스트 메서드
# 1) append()
# 리스트의 끝에 인수로 전달된 데이터 추가

my_list = ['apple', 'banana']
my_list.append('cherry')
print(my_list)


# 2) extend()
# 리스트에 다른 리스트나 튜플과 같은 반복가능객체를 추가하여 기존 리스트를 확장
print()
my_list = ['apple', 'manggo']
my_list.extend(['cherry', 'manggo'])
print(my_list)

my_list = ['apple', 'banana']
my_list += ['cherry', 'banana']
print(my_list)

# 3) insert()
# 리스트의 특정 인덱스에 데이터를 추가
print()
my_list = ['apple', 'banana']
my_list.insert(1, 'melon')
print(my_list)

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제
my_list = ['apple', 'banana']
my_list.clear()
print(my_list)

my_list = ['apple', 'banana']
my_list = []
print(my_list)

# 5) pop()
# 리스트의 마지막 요소가 반환되면서 삭제
print()
my_list = ['apple', 'banana']
i = my_list.pop()       # pop : 꺼내서 삭제하는 메서드 : 꺼냈을 때 다른 상자(변수)로 옮길 수 있음.
print(i)
print(my_list)

# 6) remove()
# 전달된 값과 동일한 요소를 찾아서 제거. 동일한 요소가 여러 개인 경우에는 첫 번째 요소가 제거
print()
my_list = ['apple', 'banana', 'cherry', 'mango']
my_list.remove('cherry')
print(my_list)

my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
my_list.renove('cherry')
print(my_list)