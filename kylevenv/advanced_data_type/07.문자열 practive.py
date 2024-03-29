# 지도 어플리케이션에서 소요시간을 크롤링 하였더니 문자열 데이터였다. 소요시간을 비교하기 위해 시간을 모두 분으로 바꾸려고 한다.
# 다음과 같이 시간이 입력되면 분으로 바꾸어주는 프로그램을 작성해보자.
# 표준입력 1시간 30분 => 표준출력 90, 표준입력 30 => 표준출력 30

time = input("시간을 입력해주세요>>>")

# 1. 분만 있는 경우 ex) 30분
# 2. 시간만 있는 경우 ex) 2시간
# 3. 시간과 분이 있는 경우 ex) 1시간 30분

if time.find('시간') == -1:
    result = int(time.split('분')[0])
else:
    if time.find('분') == -1:
        result = int(time.split('시간')[0]) * 60
    else:
        sub = time.split('시간')
        result = int(sub[0]) * 60 + int(sub[1].split('분')[0])
        print(result) 