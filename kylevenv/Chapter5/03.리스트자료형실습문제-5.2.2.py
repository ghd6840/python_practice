#5.2.2
#턱걸이 횟수를 저장할 빈 리스트를 만들고, 일주일 간의 턱걸이 횟수를 입력받아 리스트에 저장한다. 저장된 데이터의 평균을 출력한다.

count = []

x = int(input("1일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("2일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("3일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("4일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("5일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("6일차 턱걸이 횟수 >>> "))
count.append(x)
x = int(input("7일차 턱걸이 횟수 >>> "))
count.append(x)

#반복문 사용시
for i in range(1, 7):
    x = int(input(i, "일차 턱걸이 횟수 >>>"))
    count.append(x)


total = count[0] + count[1] + count[2] + count[3] + count[4] + count[5] + count[6]
avg = int(total / 7)

print("평균은",avg, "입니다")