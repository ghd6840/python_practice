#while - 반복횟수가 정해지지 않았을경우에 주로 사용

#초기식 => i = 0
#while 조건식: => while i < 10
#반복할 명령 => print(i, "번째 동작")
#증감식 => i += 1

i = 0
while i < 5:
    print(i, "등입니다.")
    i += 1

#무한루프와 break

#while True:
#    반복할 명령
#    if 조건식:
#        break

while True:
    x = input("종료하려면 exit를 입력하세요 >>>")
    if x == "exit":
        break
