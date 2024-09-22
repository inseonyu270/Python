### 인수와 매개변수 ###
# 함수로 전달되는 인수 (argument)를 저장하는 변수를 매개변수(Parameter)라고 한다.


# 1. 인수가 있는 함수
def introduce(name, age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('inseon', 10)
introduce('james', 30)


def show(*args):
    for item in args:
        print(item)


show('python')
show('happy', 'birhtday')

# 2. 디폴트 매개변수(Default parameter)
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용
# 매개변수로 기본값을 설정할 수 있다.
print()

def hello(message='안녕하세요'):
    print(message)

hello('ㅎㅇ')
hello()

# 디폴트 매개변수가 있는 경우 뒤로 배치
def hello2(name='홍길동', message='안녕하세요'):
    print(f'{name}님 {message}')
hello2()
