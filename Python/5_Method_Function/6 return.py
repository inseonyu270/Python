### 반환값 ###
# 함수 호출 결과를 반환(return value)
# 반환값이 있으면 함수 내부에서 return문을 통해 값을 반환할 수 있고
# 반환값이 없으면 함수 내부에 return문을 작성할 필요가 없다.


def address():
    str = '우편번호12345\n'
    str += '서울시 영등포구 여의도동'
    return str

address()

print(address())

def address():
    str = '우편번호12345\n'
    str += '서울시 영등포구 여의도동'
    print(str)

print(address)      # 반환값이 없기 때문에 출력이 안됨 None

# 3. 함수의 종료를 위한 return
# 반환값이 있으면 return문을 사용해 반환하고, 반환값이 없으면 return문을 생략하면 된다.
# 반환값이 없을 때도 return문을 사용하는 경우 -> 함수를 종료시킬 때

def charge(energy):
    if energy <= 0:
        print('0이하의 에너지는 충전할 수 없습니다.')
        return 
    print('에너지가 충전되었습니다.')
charge(1)
charge(-1)

# 4. 파이썬의 함수는 객체이다.
# ++) 함수는 <function>이라는 특정 자료형을 가짐. == 함수도 자료형 O
# <funtion charge at 0x0000020F3717F740>
# <funtion charge[자료형 function을 가지는 charge] at 0x0000020F3717F740 [ 주소값을 가진다 == 객체 ] >
print(charge)

# 5. 함수 안에 함수 선언도 가능하다
def print_greet(name):
    def get_greet():
        return '안녕하세요'
    print(name + '님' + get_greet())
print_greet('김철수')