#pickle 모듈
#파일에 파이썬 객체 저장하기
import pickle

data={
    "목표1" : "매일 팔굽혀펴기 100회",
    "목표2" : "매일 코딩공부 1시간"
}
file = open("./kylevenv/Chapter10/data.pickle","wb") # pickle = p = pic, w = write, b = binary
pickle.dump(data,file)
file.close()

#파일로부터 파이썬 객체 읽기
import pickle
file = open("./kylevenv/Chapter10/data.pickle","rb") # r = read
data = pickle.load(file)
print(data)
file.close()

#with구문 사용 X
#file = open("data.txt","r")
#data = file.read()
#file.close()

#with 구문 사용 O  => file.close() 따로 사용할필요없음
#with open("data.txt","r") as file:  
#    data = file.read()