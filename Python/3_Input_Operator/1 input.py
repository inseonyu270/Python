### 표준 입력 ###
# input() 함수 : 표준 입력 장치(키보드)로 부터 입력받을 때 사용
n = input('')
print(n)


n = input('정수를 입력하세요 >>>')
print(n)            # 100
print(type(n))      # <class 'str'>     : 그냥 input()를 사용해서 값을 받으면 문자열로 받음.

n = int(input('정수를 입력하세요 >>>'))     # 정수를 -- : 안내 문구 출력한 후
                                            # 입력을 받고 그 값을 int() 메서드에게 전달
                                            # 따라서 입력받은 문자열 정수값('100')을 정수화시킴 ==> 100


print(n)            # 100
print(type(n))      # <class 'int'>
