#함수를 사용하는 이유
#- 재사용성, 유지보수, 가독성

#정의하기
# def 함수이름():
#     명령블록

#호출하기
# 함수이름()

#매개변수가 있는 함수
#정의하기
#def 함수이름(매개변수1,매개변수2):
#    명령블록
#호출하기
# 함수이름(인자1,인자2)

#반환값이 있는 함수
#정의하기
#def 함수이름():         def getRandomNumber():
#    명령블록                 number = random.randint(1,10)
#    return 반환값            return number
#호출하기
# 함수이름()

#매개변수와 반환값이 있는 함수

def printMessage(name, date):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ",date,"일 남았습니다.")

printMessage("동준", 30)
printMessage("민준", 8)
printMessage("동현", 20)
printMessage("훈", 12)