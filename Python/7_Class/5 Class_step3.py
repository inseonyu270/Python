# 딕셔너리를 리턴하는 함수를 선언 ==> 박복되는 키 입력을 줄여줌.

def create_student(name, Korean, math, english, science):
    return {
        "name" : name,
        "korea" : Korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
    
# 학생의 정보를 처리하는 함수를 선언
def student_get_sum(student):
    return student["korean"] + student['math'] + student["english"] + student["science"]

def student_get_average(student):       # 평균 구함
    return student_get_sum(student) / 4

def student_to_string(student):
    return print(f'{student["name"], student_get_sum(student), student_get_average(student)}')

students = [
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 90, 94)
    ]

for student in students:
    print(student)
    student_to_string(student)