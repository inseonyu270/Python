# 1. 객체의 개념 (object)
# 객체는 모든 것. 존재하지 않는것도 객체에 해당, 객체는 상속이 가능하다
# 개발을 하다보면 정수나 실수 또는 문자열 등 기본적인 자료형을 표현하기 힘든 것들이 존재
# 예를 들어 어떤 게시글을 파이썬으로 표현을 한다면
# 게시글 번호, 제목, 작성자, 내용, 최초작성일자, 최종수정이라 , 조회수
# 이를 손쉽게 관리하려면 8개의 항목을 하나의 이름을 가진 객체(object)로 만들어서 사용하는 것이 좋다


# 2. 클래스의 개념
# 클래스 class는 객체를 만드는 도구
# 하나의 클래스를 만들어 두면 그 클래스를 통해서 (동일한 구조를 가진) 여러 개의 객체를 만들 수 있다.
# 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있다.
# 인스턴스 instancec 역시 클래스를 이용해서 생성한 객체를 가리키는 용어


# 객체와 인스턴스의 미묘한 차이
# 1) 와플머신 클래스로 만든, 와플은 객체 Object
# 2) 와플은 와플머신 클래스의 instance

# 3. 클래스 정의
# 클래스 정의 방법

# 1) Class 키워드로 클래스를 정의

# 클래스 이름은 Upper Camel Case 규칙을 따름
# 파이썬은 변수나 함수의 이름을 정할 때 언더바(_)를 이용해 단어를 연결하는 Snake Case 방식을 사용하지만
# 클래스는 Upper Camel Case 규칙을 따름
# print + member : printmember 1) print_member 2) printMember 3) PrintMember


# 클래스는 다음과 같은 형식으로 정의
# class 클래스:
# 코드

# 4. 객체 생성
# 클래스가 정의되었다면 다음과 같은 형식으로 객체를 생성
# 객체 = 클래스()

# 2개의 객체를 만들고 싶으면
# 객체1 = 클래스()
# 객체2 = 클래스()


# 5. 클래스의 정의와 객체 생성
class WaffleMachine: #waffleMachine 이라는 클래스 정의
    pass


waffle1 = WaffleMachine()       # WaffleMachine이라는 클래스를 이용해 waffle1이라는 객체 생성
waffle2 = WaffleMachine()


print( waffle1 )

# <__main__.WaffleMachine object at 0x000002199467FDA0 : 메모리의 0x000002199467FDA0번지에
# 저장된 WaffleMachine의 객체라는 읨
print( waffle2 )


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    
    def acclerate(self):
        print(self.make + "차가 가속합니다")

car_object = Car(makje="hyundai", model="SUV")
print(car_object.make)
print(car_object.model)

# car_boject = 인스턴스 : 인스턴스는 클래스로부터 생성된 구체적인 사례를 가리킨다.

# 객체 : 클래스에 기반을 두고 있으며, 클래스는 객체를 만들기 위한 템플릿
# 객체는 속성(데이터)와 메서드(동작)을 가질 수 있다.

# 인스턴스 : 특정 클래스의 구체적인 실체를 나타낸다.
# 클래스를 정의한 후에, 그 클래스를 기반으로 실제 데이터를 담는 객체를 생성하는 것을 '인스턴스화'라고 함.
# 클래스의 인스턴스로 클래스에 정의된 속성과 메서드를 실제로 사용할 수 있다.
