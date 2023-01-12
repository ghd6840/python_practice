#파일 입출력을 사용하는 이유
# - 파일로부터 데이터를 읽어와서 프로그램에 사용하기위해
# - 프로그램에서 만든 데이터를 파일형태로 저장하기 위해

#파일 열기 모드
# w : 쓰기모드(write), a : 추가모드(append), r : 읽기모드(read)
# * 파일을 열고 작업한이후에는 꼭 파일을 닫는다.

#파일 쓰기
#파일객체 = open("파일이름","파일모드")
#파일객체.write(데이터)
#파일객체.close()
file=open("./kylevenv/Chapter10/data.txt","w", encoding="utf8")   # * w = 덮어쓰기
file.write("1.파이썬 공부")
file.close()

#파일 추가
file=open("./kylevenv/Chapter10/data.txt","a", encoding="utf8") # * a = 이어쓰기
file.write("\n2.파이썬 공부하기")
file.close()

#파일 읽기
#파일객체 = open("파일이름","파일모드")
#변수 = 파일객체.read()
#파일객체.close()

#3 파일읽기
file=open("./kylevenv/Chapter10/data.txt","r", encoding="utf8") # * 파일 전체 읽기

#3.1 파일전체읽기
data = file.read()
print(data)
file.close()

#3.2 파일 한 줄 읽기()
file=open("./kylevenv/Chapter10/data.txt","r", encoding="utf8")
while True:
    data = file.readline()
    print(data)   # print(data, end="") end를 이용해서 줄바꿈 스페이스 없앰.
    if data == "":
        break
file.close()