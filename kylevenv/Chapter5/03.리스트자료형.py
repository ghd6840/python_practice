#리스트
#리스트명 = [] 
#데이터추가  = 리스트.append(데이터), 데이터 할당 리스트[인덱스] = 데이터, 데이터 삭제 = del 리스트[인덱스], 슬라이싱 리스트[시작:끝+1], 리스트 길이 len(리스트), 리스트 정렬 리스트.sort()

#데이터 있는 리스트
animals = ["코끼리","하마","코뿔소","곰"]
#데이터 없는 리스트
empty = []

#인덱스로 값 호출
print(animals[2])
print(animals[-1])

#데이터 추가하기
animals.append("호랑이")

#데이터 할당
animals[1] = "사자"

#데이터 삭제
del animals[2]
print(animals)

#리스트 슬라이싱
print(animals[1:3])
print(animals[:]) # 전체
print(animals[:3]) # 0부터
print(animals[0:]) # 끝까지

#리스트 길이
print(len(animals))

#리스트 정렬
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)