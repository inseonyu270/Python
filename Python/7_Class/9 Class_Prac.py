# 사용자가 what 메서드를 통해 입력한 시간은 "HH:MM"
# " 형식으로 입력되어야 합니다. 예를 들어 "10:30:45".
# 시간을 입력할 때 시, 분, 초는 모두 정수형으로 저장되어야 합니다.
# see 메서드를 호출하여 출력할 때 시간은 "HH시 MM분 SS초" 형식으로 출력되어야 합니다. 예를 들어 "10시 30분 45초"

# watch 클래스를 만들어라 !!
# what() Method : 시간을 입력하세요 >>> 12:12:31
#               : 시간을 사용자에게 물어보고 그 시간을 객체의 hour, minute, second라는 속성을 추가하는 기능을 가짐
# see() Method  : 계산된 시간은 12시 12분 31초입니다.를 출력

class Watch:
    def What(self):
        time_input = input("시간을 입력하세요 >>> ")
        h, m, s = time_input.split(':')
        self.hour = int(h)
        self.minute = int(m)
        self.second = int(s)
        
    def see(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다')

# 풀이
# class Watch:
#     def What(self):
#         hms = input('시간을 입력해주세요 >>> ')             # 12:12:31
#         list = hms.split(':')                             # ["12", "12", "31"]
#         self.hour = int(list[0])
#         self.minute = int(list[1])
#         self.second = int(list[2])
#     def see(self):
#         print(f'{self.hour}시 {self.minute}분 {self.second}초입니다.')



watch = Watch()
watch.What()
watch.see()
