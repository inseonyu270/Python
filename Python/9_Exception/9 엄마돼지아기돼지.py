# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서
# '꿀' 이라는 글자가 몇 번 나오는지 찾는 프로그램입니다.

# hint : 문자 자체를 받으려면 문자열을 먼저 추출 후 문자를 추출하는 형식이여야 한다.

file = open('./9_Exception/input/엄마돼지아기돼지.txt', 'rt', encoding='utf-8')

count = 0

while True:
    str = file.read(1)

    if str == "꿀":
        count += 1

    if not str:
        print(f"꿀의 횟수 : {count}")
        break
file.close


# ++) readlines() 메서드를 구글링 후 활용해서 위 문제 해결

lines = file.readlines()

l_count = 0

for line in lines:
    l_count += line.count("꿀")

print(f'꿀의 횟수 {l_count}')
file.close

#풀이)

# with open('./9_Exception/input/엄마돼지아기돼지.txt', 'rt', encoding='utf-8')

# 방법 1) 전체를 읽어와서 개수 세기

str = file.read()
cnt = str.count("꿀")
print(cnt)
file.close

# 방법 2) 짧게 끊어서 개수 세기

cnt = 0
while True:
    str = file.read(5)
    if not str:
        break
    cnt += str.count("꿀")

print(cnt)
file.close


# 방법 3) readlines() 사용하는 방법
# while True:가 필요할까? ==> X

line_list = file.readlines()            # line_list는 모든 텍스트 파일안의 가사들을 가지고 있음.
                                        # ==> 텍스트 파일 안의 모든 문장을 읽어왔다.
#[                              #리스트의 시작

                                # 리스트의 인덱스
# '토실토실 아기돼지\n',    #0
# '밥달라고 꿀꿀꿀\n',      #1
# '엄마돼지 오냐오냐\n',    #2
# '알았다고 꿀꿀꿀\n',      #3
# '\n',                    #4
# '\n',                    #5
# '꿀꿀 꿀꿀 꿀꿀 꿀꿀\n',  #6
# '꿀꿀꿀꿀 꿀꿀꿀꿀\n'     #7
# '꿀꿀꿀꿀꿀'              #8 

# ]         # 리스트의 끝

print(line_list)

# Tips) 리스트 형태의 요소들을 하나씩 꺼내기 위해서는 for문을 사용했음.

cnt = 0
for line in line_list:
    cnt += line.count("꿀")
print(cnt)
file.close

# 방법 4) 문자를 하나씩 끊어서 꿀인지 확인하고 꿀이라면 개수를 증가

total = file.read()
cnt = 0

for char in total:      # 한글자씩 for문으로 반복해서 char에 담기
    if char == '꿀':
        cnt += 1
    
print(f'꿀의 횟수 : {cnt}')