### 파일 출력 output ###

# 1. 텍스트 파일 생성
file = open('./9_Exception/output/hello.txt', 'wt', encoding='utf-8')


file.write('안녕하세요')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
file.write('hello.txt 파일이 생성되었습니다.')

file.close()

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a모드(append)
file = open('./9_Exception/output/hello.txt', 'at', encoding='utf-8')

file.write('Hello\n')
file.write('hello.txt 파일에 새로운 내용이 추가되었습니다.')