# 수학여행을 어디로 갈지 결정하기 위해 학생들이 희망하는 모든 수학여챙 장소를 조사하기로 했습니다.
# 학생들이 원하는 장소를 입력받아 동일한 입력은 무시하고 모든 입력을 저장하려고 합니다.
# 학생을 4명으로 가정하고 실행 예와 같이 동갖하는 프로그램을 구현하세요

# 희망하는 수학 여행지를 입력하세요 >>> 에버랜드
# 희망하는 수학 여행지를 입력하세요 >>> 이월드
# 희망하는 수학 여행지를 입력하세요 >>> 블루원
# 희망하는 수학 여행지를 입력하세요 >>> 이월드

# 조사된 수학 여행지는 {'에버랜드', '이월드', '블루원'}

## list ##
math = []

math.append(input('희망하는 수학 여행지를 입력하세요 >>> '))
math.append(input('희망하는 수학 여행지를 입력하세요 >>> '))
math.append(input('희망하는 수학 여행지를 입력하세요 >>> '))
math.append(input('희망하는 수학 여행지를 입력하세요 >>> '))

print('조사된 수학 여행지는 {p_math}'.format(p_math=set(math)))

## Set ##
# math_set = set()

# math_set.add(input('희망하는 수학 여행지를 입력하세요 >>> '))
# math_set.add(input('희망하는 수학 여행지를 입력하세요 >>> '))
# math_set.add(input('희망하는 수학 여행지를 입력하세요 >>> '))
# math_set.add(input('희망하는 수학 여행지를 입력하세요 >>> '))

# print(f'조사된 수학 여행지는 {math_set}')