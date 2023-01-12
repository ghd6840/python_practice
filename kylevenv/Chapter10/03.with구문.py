#with구문 사용 X
#file = open("data.txt","r")
#data = file.read()
#file.close()

#with 구문 사용 O  => file.close() 따로 사용할필요없음
with open("./kylevenv/Chapter10/data.txt","r",encoding='utf8') as file:  
    data = file.read()
    print(data)