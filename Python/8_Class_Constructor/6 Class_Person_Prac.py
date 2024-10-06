# class Person
# 클래스 변수 : count : 0
# 객체를 만들어질 때마다 클래스 변수 count가 1씩 증가해야함

# 객체를 print(하게 되면)   "객체이름 is born"   이라는 문구가 출력

# 객체를 지울 때 마다       "객체이름 is dead"   이라는 문구가 출력

# 클래스 메서드 :get_population() : 클래스 변수 count를 변환


class Person:
    person_count = 0
    
    def __init__(self, name):
        Person.person_count += 1
        self.name = name
    
    def __str__(self):
        return f'{self.name} is born'
    
    def __del__(self):
        print(f'{self.name} is dead')
        Person.person_count -= 1
    
    @classmethod
    def get_population(cls):
        return cls.person_count


man = Person('james')
print(man)      # james is born
woman = Person('emily') 
print(woman)    # emily is born

print(f'전체 인구수 : {Person.get_population()}명')

del man
print(f'전체 인구수 : {Person.get_population()}명')