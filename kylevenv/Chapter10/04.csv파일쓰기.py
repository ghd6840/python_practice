#csv = comma-separated values

#csv 파일 쓰기
import csv

data = [
    ["이름","반","번호"],
    ["재석",1,20],
    ["홍철",3,7],
    ["형돈",5,32]
]

file = open("./kylevenv/Chapter10/student.csv","w", newline="", encoding="utf-8-sig")  # newline, encoding은 window를 위해서.
writer = csv.writer(file)
for d in data:
    writer.writerow(d)
file.close()