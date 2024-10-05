# 생성자와 소멸자를 이용해서 서비스 안내 메시지를 출력하는 프로그램


class Service:
    def __init__(self, service):
        self.service = service
        print(f'{self.service}가 시작되었습니다.')

    
    def __del__(self):
        print(f'{self.service}가 종료되었습니다.')


s = Service('길 안내')
# 객체를 생성할 때 생성자를 호출해 '길 안내가 시작되었습니다'
# 코드의 실행을 마치면 객체 s는 자동으로 소멸, 따라서 소멸자가 호출돼 '길 안내가 종료되었습니다' 
