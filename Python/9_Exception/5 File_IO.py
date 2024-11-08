# 1. 파일 열기
# 입출력 파일을 저장하는 것을 의미. 파일 객체 생성
# 파일 입력과 출력을 모두 반드시 파일 열기 작업을 가장 먼저 수행


# 파일 객체 = open(파일명, 모드)


# 1) 파일명
# 입출력 작업을 수행할 파일을 의미
# 파일명만 작업할 수도 있고 경로를 함께 작성할 수도 있다.

# 파일명만 작성하는 경우 : 파이썬 소스 파일과 같은 경로에 존재하는 경우
# open('sample.txt')

# 전체 경로로 작성하는 경우
# open('C:/.....')

# 현재 디렉터리(.)을 기준으로 경로를 지정
# open('./sample.txt')


# 2) ahem
# -------------------
# 입력
# -------------------
# r (read) 읽기


# -------------------
# 출력
# -------------------
# w (write) 쓰기 (파일이 있으면 새로 생성, 없어도 새로 생성) 만약 파일이 있는 경우 덮어쓰기가 된다.
# a (append) 추가 (파일이 있으면 추가, 없으면 새로 생성) 
# x (exclusive) 베타적 추가 (파일이 있으면 오류, 없으면 새로 생성)


# 파일의 종류
# t (text) 텍스트 파일
# b (binary) 바이너리 파일 (텍스트 파일외의 모든 파일)

# 2. 파일 닫기
# 파일을 더 이상 사용하지 않거나 프로그램을 종료하고자 할 때
# 파일이름.close()

# 3. 파일 생성

# from pathlib import Path
# print(Path.cwd())
file = open('./9_Exception/output/my_file.txt', 'wt')
print('my_file.txt 파일이 생성되었습니다.')