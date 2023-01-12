#csv 파일 읽기
import csv

file = open("./kylevenv/Chapter10/student.csv","r", newline="", encoding="utf-8-sig")
reader = csv.reader(file)
for d in reader:
    print(d)
file.close()