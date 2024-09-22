# MTLES, POUND는 단위 변환에서 사용하는 변수

MILES = 0.621371
POUND = 0.002205

# 킬로미터를 마일로 변환
def kilometer_to_miles(kilometer):
    return kilometer * MILES


# 그램을 파운드로 변환하는 함수
def gram_to_pounds(gram):
    return gram * POUND