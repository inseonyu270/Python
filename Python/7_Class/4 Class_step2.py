# 딕셔너리를 리턴하는 함수를 선언 ==> 반복되는 키 입력을 줄여줌.


def create_student(name, Korean, math, english, science):
    return{
        "name" : name,
        "Korean" : Korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
    
students = {
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 90 ,94)
}

# 학생을 한명씩 반복하면서 출력
for student in students:
    # 점수의 총합과 평균을 구함
    score_sum = student["Korean"] + student["math"] + student['english'] + student['science']
    score_average = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_average, sep='\t\t')