#팔굽혀펴기 개수
result = [33,40,12,63,52]

#문항 1 6번의 팔굽혀펴기 개수는 9개이다. 리스트의 마지막에 추가
result.append(9)
print(result)

#문항 2 2번은 재측정하여 50개를 하였다. 2번의 데이터를 변경해보자
result[1] = 50
print(result)

#문항 3 3번부터 6번까지 데이터를 슬라이싱하자.
print(result[2:])

#문항 4 모든 데이터를 오름차순으로 정렬하자.
result.sort()
print(result)