class MyClass:
    # self : 특별한 예약어. 클래스의 인스턴스 메서드 안에서 사용된다.
    # 해당 메서드가 호출된 인스턴스를 가리킨다. self는 현재 인스턴스를 나타냄.
    # 생성자(__init__) : 겍처가 만들어질 때 무조건적으로 실행되는 함수
    # self.value = MyClass의 값
    def __init__(self, value):
        self.value = value
    def print_value(self):
        print(self.value)

obj = MyClass(42)
obj.print_value()
obj1 = MyClass(99)
obj1.print_value


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name            # Student 객체의 이름 속성을 추가
        self.korean = korean
        self.math = math
        self.englsih = english
        self.science = science
        
        def get_sum(self):
            return self.korean + self.math + self.english + self.science
        
        def get_average(self):
            return self.get_sum() / 4
        
        def to_string(self):
            # \t : 탭키만큼 이동시킨다.
            return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'


students = {
    Student("연하진", 92, 96, 98, 100),
    Student("구지연", 76, 96, 94, 90)
}

for student in students:
    print(student)
    print(student.to_string)
