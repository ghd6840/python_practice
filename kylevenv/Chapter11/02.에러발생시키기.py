# raise 구문 사용법
#raise 예외("에러메세지")
#raise Exception
#raise Exception("에러 메세지")

# raise  구문을 사용해서 에러를 발생시켜보기

try:
    num = int(input("음수를 입력해 주세요 >>> "))
    if num >= 0:
        raise Exception("양수는 입력 불가") #Exception => ValueError 맞춰서 사용하면 됨
except Exception as e:
    print("에러발생!", e)
