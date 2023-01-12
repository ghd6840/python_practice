# Unit 클래스
class Unit:
    """
    속성 : 이름, 득점, 리바운드, 어시스트
    """

    # 생성자 (constructor)
    # 객체를 생성할 때 호출되는 매서드
    def __init__(self, name, score, rebound, assist):
        self.name = name
        self.score = score
        self.rebound = rebound
        self.assist = assist
        print(f"[{self.name}] 선수의 기록이 등록됐습니다.")

    def __str__(self):
        return f"[{self.name}] 득점: {self.score}, 리바운드: {self.rebound}, 어시스트: {self.assist}"
        

# 객체 생성
kd = Unit("Kevin Durant", 30, 8, 7)
lj = Unit("Lebron James", 27, 10, 10)
kl = Unit("Kaway Leneord", 25, 6, 7)

print(kd)
print(lj)
print(kl)