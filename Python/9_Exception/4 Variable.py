# 변수는 프로그램을 실행할 때 데이터를 저장하기 좋은 방법이다.
# 그러나 프로그램을 종료한 후에도 데이터를 유지하고싶은 경우, 파일 형태로 저장해야 한다.



# 1. 파일과 파일 경로
# 파일에는 파일 이름과 경로라는 두 가지 주요 속성이 있다.


# 예를 들어 윈도우 운영체제를 사용하는 컴퓨터의 경우
# C:\inseonyu270\python\9_Exception 이라는 경로에 4 Variable.py 파일이 있는 경우
# 파일 이름 : 4 Variable.py 
# 폴더 (디렉터리, 디렉토리) 이름 : inseonyu270, python, 9_Exception
# 폴더 안에는 파일이나 다른 폴더가 들어 있을 수 있음.


# 경로의 C:\는 루트 폴더를 나타내며 모든 폴더가 이 안에 있음
# 윈도우에서 루트 폴더의 이름은 "C:\"이며 C 드라이브라고 부름.
# 윈도우, 맥OS에서는 폴더이름이나 파일이름의 대소문자를 구분하지 않지만,
# 리눅스는 구분함.

# 윈도우에서 폴더 구분은 \ : 백슬래쉬로 사요ㅕㅇ하고, 맥 OS나 리눅스에서는 "/" 슬래쉬를 사용함.
# 프로그램의 모든 운영체제에서 작동하게 하려면 "\", "/" 두가지 경우를 모두 처리하도록 코드를 작성하는게 좋음


# 모듈 #
# pathlib : 파일 시스템 경로를 객체 지향적으로 다룰 수 있게 도와주는 모듈
#         : 여기서는 현재 작업 디렉터리를 가져오기 위해 사용됨


# platform : 시스템의 플랫폼 관련 정보를 가지고 올 수 있게 해주는 모듈
#          : 여기서는 운영체제 정보를 확인하기 위해 사용됨.


from pathlib import Path
import platform

print(Path.cwd())             # cwd(curretn working dicrectory) : 현재 파이썬이 실행되는 경로를 반환(알려줌)

my_os = platform.system()   # system() : 운영체제의 이름을 문자열로 반환
                            # windows == windows
                            # macOS == Darwin
                            # Linux == Linux
print("OS가 무엇인가? : ", my_os)

if my_os == "Windows":
    print('windows 운영체제입니다.')
else:
    print('다른 운영체제입니다.')


# 절대 경로와 상대 경로 #
# 절대 경로 : 항상 루트 폴더에서 시작하는 경로
# 상대 경로 : 현재 작업 디렉터리에 대한 경로


# os.makedirs() 함수로 새로운 디렉터리(폴더)를 만들 수 있다.
# os.path.isdir(path) : path의 디렉터리가 있는지 확인

# '.' : 현재 리텍터리
# '..' : 상위 디렉터리
# '...' : 상위 디렉터리의 상위 디렉터리

import os

# './' : 현재 디렉터리를 가리킨다.
path = './input'
if not os.path.isdir(path):         # path의 디렉터리가 없다면~
    os.makedirs(path)               # 현재 작업 폴더 안에 input이라는 폴더를 생성


path = './9 Exception/4 Variable.py'
# os.path.getsize(path)             : path 인자에 해당되는 파일 크기를 바이트(byte) 단위로 변환
print(os.path.getsize(path))

# os.listdir(path)                  : path에 있는 파일 이름 리스트로 반환
path = './9_Exception'
print(os.listdir(path))
