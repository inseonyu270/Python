# 학생 리스트를 선정,  딕셔너리 요소로 가진 리스트

students = [
    {"name" : "연하진", "Korean" : 92, "math" : 98, "english" : 96, "science" : 98},
    {"name" : "구지연", "Korean" : 76, "math" : 96, "english" : 94, "science" : 98},
    {"name" : "나선주", "Korean" : 98, "math" : 92, "english" : 96, "science" : 92},
    {"name" : "윤아린", "Korean" : 95, "math" : 98, "english" : 98, "science" : 98},
    {"name" : "윤명월", "Korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]

# 학생을 한명씩 반복하면서 출력
for student in students:
    # 점수의 총합과 평균을 구함
    score_sum = student["Korean"] + student["math"] + student['english'] + student['science']
    score_average = score_sum / 4
    # 출력
    print(student["name"], score_sum, score_average, sep='\t\t')