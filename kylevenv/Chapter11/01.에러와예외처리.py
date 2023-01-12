#try : 예외가 발생할수 있는 코드
#except : 예외 발생 시 실행할 코드
#else : 예외 발생하지 않은 경우 실행할 코드
#finally: 항상 실행할 코드

# 원화를 입력, 환율 입력 -> 달러값

won = input("원화금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요 >>> ")

try:
    print(int(won) / int(dollar))
except: #ValueError 에러값 사용가능
    print("예외가 발생했습니다.")


try:
    print(int(won) / int(dollar))
except ValueError as e: #ValueError 에러값 사용가능
    print("문자열 예외가 발생했습니다.")
except ZeroDivisionError as e:
    print("나누기 0은 불가능합니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("항상 실행됩니다.")

