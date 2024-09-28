# 클래스 도입의 필요성

# 학생의 정보를 출력하는 함수

def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = 'emily'
department1 = 'computer engineering'
professor1 = 'james'
address1 = 'seoul'
phone1 = '010-1234-5678'
grade1 = 'A'

student_info(name1, department1, professor1, phone1, address1, grade1)

name2 = 'alice'
department2 = 'computer engineering'
professor2 = 'david'
address2 = 'busan'
phone2 = '010-4321-4321'
grade2 = 'B'

student_info(name2, department2, professor2, phone2, address2, grade2)

# 함수가 추가될 때 마다 변수를 생성해야 하고 관리가 어려움