class Monster:
    def say(self):
        print("나는 몬스터다")

goblin = Monster()
goblin.say()

#파이썬에서는 자료형도 클래스다
a = 10
b = "문자열 객체"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__()) # __dir__() 문자열에서 사용할수있는 메서드가 나오게 됨