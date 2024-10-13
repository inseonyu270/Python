### 1. 텍스트 파일 읽기 ###
# 1) read() 메서드
# file.read(size)
# 파일로부터 데이터를 읽어오는 메서드

file = open('./9_Exception/input/hello.txt', 'rt', encoding='utf-8')

str = file.read()     # 파일 전체를 한번에 읽어들임.
print(str)


file.close()

# read() 메서드를 통해 전체를 읽으려면 그 만큼 메모리 공간을 필요
# 읽어야 할 파일이 크다면 일부만 읽어 들이는 작업을 반복하는 반복문을 사용하여
# 파일 전체를 읽도록 구현하는 것이 좋다.


file = open('./9_Exception/input/엄마돼지아기돼지.txt', 'rt', encoding='utf-8')

while True:
    str = file.read(5)      # file.read(5)는 파일에서 5바이트만큼 데이터를 읽어온다.
    if not str:
        break
    print(str, end='')

file.close()
