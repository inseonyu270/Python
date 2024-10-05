### 클래스 메서드와 정적 메서드 ###

# 1. 클래스 변수
# 클래스를 구현할 때 인스턴스마다 서로 다름 값을 가지는 경우에는 인스턴스 변수를 사용


# 모든 인스턴스 변수들은 self 키워드를 붙여서 사용

# 모든 인스턴스가 동일한 값을 사용할 때는 클래스 변수로 처리해서
# 모든 인스턴스들이 공유하도록 처리하는 것이 좋음.


# 인스턴스 변수는 인스턴스마다 값을 별도로 저장해야 하지만
# 클래스 변수는 하나의 값을 모든 인스턴스가 공유하기 때문에 메모리 공간의 낭비를 막을 수 있음.

class Korean:
    country = '한국'        # 클래스 변수 country
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

print(Korean.country)

student1 = Korean('홍길동', 35, '대구')
print(student1.name)
print(student1.country)

print(student1.name, student1.age, student1.address, student1.country)
print()





print('객체 프로퍼티 생성과 동일한 이름의 클래스 변수')
student1.country = '미국'       # 객체의 변수 생성
print(student1.country)         # 클래스 변수를 불러오는 것이 아니라 인스턴스 변수를 불러왔기 때문.
                                # student1 객체의 country라는 인스턴스 변수와 country 클래스 변수 2개가 존재
print(student1.__class__.country)   # 한국.객체를 사용해서 클래스 변수 불러왔기 때문


print()

student1.company = '삼성'       # 객체의 프로퍼티 생성
print(student1.company)

student1.__class__.country = '영국'
print(Korean.country)
print()



print('클래스를 이용해서 클래스 변수값 변경')
Korean.country = '미국'             # 클래스 변수를 변경

man2 = Korean('홍길동2', 35, '서울')
print(man2.country)
print(Korean.country)
print()


class Student:
    school = '서울대학교'

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):             # 인스턴스 자체를 받으면 원래는 주소값이 뜨지만,
                                   # __str__ 함수는 인스턴스 자체를 출력하면 return 된 값을 보여준다.
        return f'{Student.school} {self.grade}학년 {self.name}'
    
hong = Student('홍길동', 3)
print(hong)

kim = Student('김선우', 2)
print(kim)

print(hong.school)
hong.school = '경북대학교'      # 클래스 변수가 변경된게 아니라 hong이라는 인스턴스에 school이라는 속성이 추가됨.
print(hong.school)             # 프로퍼티(속성)이 추가된 후 hong.school ==> 경북대학교
print(hong.__class__.school)   # 클래스(cls)




### 2. 클래스 메서드 ###
# 클래스 변수를 사용하는 메서드를 의미

# 주요 특징 #
# 1. 인스턴스 혹은 클래스로 호출
# 2. 생성된 인스턴스가 없어도 호출할 수 있음.
# 3. @classmethod 데코레이터 decorator를 표시하고 작성
# 4. 매개변수 self를 사용하지 않고 cls를 사용
# 클래스 메서드는 self를 사용하지 않기 때문에 인스턴스 변수에 접근할 수 없지만
# cls를 통해 클래스 변수에 접근할 수 있음.


class Korean:
    country = '한국'

    @classmethod
    def trip(cls, country):

        if cls.country == country:
            print('국내 여행입니다.')
        else:
            print('해외 여행입니다.')

Korean.trip( '한국')         # 클래스 메서드 == 객체 없이 사용 가능한 메서드 == 따라서, 객체(인스턴스)의 변수들이 있으면 X
                            # 왜냐하면 객체가 있어야 인스턴스가 있는데 객체가 지금 없는 상태에서 사용가능한 메서드가 클래스 메서드
                            # 따라서 인스턴스 변수는 사용이 X
Korean.trip('미국')


### 3. 정적 메서드 (static method) ###

# 1) 인스턴스 또는 클래스로 호출
# 2) 생성된 인스턴스 없어도 호출 가능
# 3) 정적 : 정 : 정지하다. @staticmethod 데코레이터 decorator를 표시하고 작성
# 4) 반드시 작성해야 할 매개변수가 없다.


# 정적 메서드는 self와 cls를 모두 사용하지 않기 때문에
# 인스턴스 변수와 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적절

# 정적 메서드는 클래스에 소속이 되어 있지만,
# 인스턴스에는 영향을 주지 않고 또 인스턴스로 부터 영향을 받지도 않는다.

class Korea:
    country = '한국'

    @staticmethod
    def slogan():
        print('Korean')

Korean.slogan()

























