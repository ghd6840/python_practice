#5.1.4
#프로그램 사용자로부터 국어 수학 영어 성적 입력
#세과목 평균점수가 80점이상 합격
#합격, 불합격 정해지는 프로그램에 오류발생. 80점이 안되일경우 불합격표시
#단, 0점에서 100점 사이의 숫자를 입력하지않으면 "잘못입력하셨습니다" 출력

korean = int(input("국어 >>> "))
math = int(input("수학 >>> "))
eng = int(input("영어 >>> "))

sum = (korean + math + eng) / 3

#방법 1
if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    if sum >= 80:
        print("불합격입니다.")
    else:
        print("합격입니다.")
else:
    print("잘못 입력하셨습니다.")

#방법 2
if korean < 0 or korean > 100 or math < 0 or math > 100 or eng < 0 or eng > 100:
    print("잘못 입력하셨습니다.")
elif sum >= 80:
    print("불합격입니다.")
else:
    print("합격입니다.")