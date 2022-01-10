#8.1.1

#아이템 공통 : 이름,가격,무게,판매하기,버리기
#장비 아이템 : 착용효과, 착용하기
#소모품아이템 : 사용효과, 사용하기

class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"[{self.name}] 착용. {self.effect}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}] 사용했습니다. {self.effect}")

# 인스턴스 생성
cap = WearableItem("모자", 4000, 4, True, "체력 2000증가")
cap.wear()
cap.sale()
cap.discard()

potion = UsableItem("신비한투명물약",50000, 0.1, False, "투명효과 200초 지속")
potion.discard()
potion.sale()
potion.use()
