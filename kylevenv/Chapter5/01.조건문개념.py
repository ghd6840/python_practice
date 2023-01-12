#조건문
# : 조건에 따라 실행할 명령이 달라지는 것

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass:
    print("로그인 성공")
    print("안녕하세요~")
elif input_pass == "":
    print("비밀번호를 입력하세요!")
else:
    print("로그인 실패")
    print("비밀번호를 확인해주세요~")