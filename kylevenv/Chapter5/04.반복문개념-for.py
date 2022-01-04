#시퀀스 자료형
#순서가있는 자료형, 리스트, 문자열, range객체, 튜플, 딕셔너리

#for 변수 in 시퀀스 자료:
#for a in [1,2,3,4]:
#    print(a)

#range 명령어
#range(10) = 0~9까지 숫자를 포함하는 range 객체를 만들어 준다.

#for 문
# - 리스트 사용
teams = ["아스날","첼시","맨유"]

for team in teams:
    print("선택한 팀은",team,"입니다")

# - 문자열 사용
message = "하나씩 차분히"

for word in message:
    print(word)

# - range 객체 사용
# range(10), range(시작, 끝+1), range(시작, 끝+1, 단계)
for i in range(10):
    print(i)