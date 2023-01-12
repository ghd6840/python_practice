# Player 클래스 구현
# 속성: 닉네임, 미네랄, 가스, 유닛리스트

unit_info = {
    "probe":{
        "name": "프로브",
        "mineral": 50,
        "gas": 0,
        "hp": 20,
        "shield": 20,
        "demage": 5
    },
    "zealot":{
        "name": "질럿",
        "mineral": 100,
        "gas": 0,
        "hp": 100,
        "shield": 60,
        "demage": 16
    },
    "dragon":{
        "name": "드라군",
        "mineral": 125,
        "gas": 50,
        "hp": 100,
        "shield": 80,
        "demage": 20
    }
}

class Unit : 
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
    
class Player:
    def __init__(self, nickname, mineral, gas, unit_list=[]):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def product(self, name, mineral, gas, hp, shield, demage):
        if self.mineral - mineral < 0 :
            print('미네랄이 부족합니다')
        elif self.gas < 0 :
            print('가스가 부족합니다')
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name, hp, shield, demage)
            self.unit_list.append(unit)
            print(f"[{name}]을(를) 생산합니다.")

# 플레이어 생성
Player1 = Player("Bisu", 400, 10)

# 유닛 생성
Player1.product(unit_info['probe']['name'], unit_info['probe']['mineral'], unit_info['probe']['gas'],unit_info['probe']['hp'], unit_info['probe']['shield'], unit_info['probe']['demage'])

Player1.product(unit_info['zealot']['name'], unit_info['zealot']['mineral'], unit_info['zealot']['gas'],unit_info['zealot']['hp'], unit_info['zealot']['shield'], unit_info['zealot']['demage'])

Player1.product(unit_info['dragon']['name'], unit_info['dragon']['mineral'], unit_info['dragon']['gas'],unit_info['dragon']['hp'], unit_info['dragon']['shield'], unit_info['dragon']['demage'])

for unit in Player1.unit_list:
    print(f"[{unit.name}] 의 체력 {unit.hp} 방어력 {unit.shield} 공격력 {unit.demage} 입니다.")