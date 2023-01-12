#상속 심화
#클래스 변수
# - 인스턴스들이 모두 공유하는 변수

import random
#부모클래스 정의
class Monster:
    max_num = 1000
    def __init__(self,name,health,attack):  #속성
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")              #메서드 - 이동하기

#자식클래스 정의
class Wolf(Monster):
    pass   # 수정할내용이 없거나 할때 그대로 사용할수있음

class Shark(Monster):
    def move(self):  #메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    #생성자 오버라이딩
    def __init__(self,name,health,attack):   # def __init__(self,name,health,attack,skill
        super().__init__(name,health,attack)
        self.skills = ("불뿜기","꼬리치기","날개치기")                       # self.skills = skill
        
    def move(self):   #메서드 오버라이딩
        print(f"[{self.name}] 날기")
    
    def skill(self):
        print(f"[{self.name}] 스킬사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프", 1500, 250)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크", 1300, 350)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 2000, 300)
dragon.move()
dragon.skill()