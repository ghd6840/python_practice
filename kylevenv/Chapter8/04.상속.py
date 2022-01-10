#상속 : 부모클래스 - 속성 메서드 -> 자식클래스 - 속성 메서드
# - 클래스들에서 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용.

#부모클래스 정의
class Monster:
    def __init__(self,name,health,attack):  #속성
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")              #메서드 - 이동하기

#자식클래스 정의
class Wolf(Monster):
    pass   # 수정할내용이 없거나 할때 그대로 사용할수있음

class Shark(Monster):
    def move(self):  #메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):   #메서드 오버라이딩
        print(f"[{self.name}] 날기")

wolf = Wolf("울프", 1500, 250)
wolf.move()

shark = Shark("샤크", 1300, 350)
shark.move()

dragon = Dragon("드래곤", 2000, 300)
dragon.move()