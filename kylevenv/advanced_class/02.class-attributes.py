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
    def __init__(self, name, score, rebound, assist):
        self.name = name
        self.score = score
        self.rebound = rebound
        self.__assist = assist
        Unit.count += 1
        print(f"[{self.name}] 선수의 기록이 등록됐습니다.")

    def __str__(self):
        return f"[{self.name}] 득점: {self.score}, 리바운드: {self.rebound}, 어시스트: {self.__assist}"
        
kd = Unit("Kevin Durant", 30, 8, 7)
lj = Unit("Lebron James", 27, 10, 10)
kl = Unit("Kaway Leneord", 25, 6, 7)

# 인스턴스 속성 수정
kd.rebound -= 1
print(kd)

# 전체유닛 개수
print(Unit.count)

# 비공개 속성 접근
kl.__assist = 888
print(kl)

# 네임 맹글링 (name mangling)
kl._Unit__assist = 8
print(kl)