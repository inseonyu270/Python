
# 출력하고자 하는 구구단을 입력받아 구구단을 출력(단 while문 사용 금지)
# 실행 예 : 출력할 구구단을 입력하세요 >> ex) 5단 -> 5단만 출력

num = int(input("출력할 구구단을 입력하세요 >>> "))

for i in range (1 , 10, 1):
    print(f"{num} * {i} = {num * i}")



# # 1부터 5 사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현하세요.

for i in range (5 , 0, -1):
    print(f"{i}")


# 사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 1부터 입력받은 정수까지 
# 모든 정수의 합계를 출력하는 프로그램을 구현하세요.

num = int(input("임의의 양의 정수 입력 : "))
sum = 0

for i in range (1, (num + 1), 1):
    sum += i
print(f"1부터 {i}까지의 모든 정수의 합계는 {sum}입니다.")

# 실행 예)
# 임의의 양수를 입력하세요 >>> 5
# 1부터 5까지의 모든 정수의 합계는 15입니다.

num = int(input("임의의 양수를 입력하세요 >>> "))
sum = 0

for i in range (1, (num + 1), 1):
    sum += i
print(f"1부터 {i}까지의 모든 정수의 합계는 {sum}입니다.")

# 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일이름' 을 입력받아 'basket'리스트
# 저장하는 프로그램을 구현하세요 

num = int(input("임의의 양의 정수 입력 : "))
name = [ ]

for i in range (1, (num + 1), 1):
    fruit = input("과일 이름 : ")
    name.append(fruit)
print(name)
