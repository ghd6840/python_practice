class Unit:
    """
    인스턴스 속성 : 이름, 득점, 리바운드, 어시스트
    -> 객체마다 다른 값을 가지는 속성

    클래스 속성 : 전체 유닛 개수
    -> 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스안에서만 사용가능
    """

    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f"[{self.name}] 유닛이 등록됐습니다.")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}"
    
    # 1. instance method - 항상 첫 파라미터로 self - 인스턴스 속성에 접근할수 있는 메서드
    def hit(self, demage):
        #방어막 변경
        if self.shield >= demage:
            self.shield -= demage
            demage = 0
        else:
            demage -= self.shield
            self.shield = 0

        # 체력 변경
        if demage > 0:
            if self.hp > demage:
                self.hp -= demage
            else:
                self.hp = 0

    # 2. class method - 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]개")

zealot = Unit('Zealot', 100, 80, 20)
probe = Unit('Probe', 20, 5, 5)
scv = Unit('Scv', 60, 4, 5)

probe.hit(16)
print(probe)
probe.hit(30)
print(probe)

Unit.print_count()

# magic method
print(dir(probe))