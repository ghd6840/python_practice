# 리스트 할당 방식

x = [1,2,3,4,5]
y = x

y[2] = 0

print(x)
print(y)
print(id(x))
print(id(y))

# 리스트 복사 방식
x = [1,2,3,4,5]
y = x.copy()
print(x)
print(y)

# 다차원(중첩) 리스트 복사
import copy
x = [[1,2],[3,4,5]]
y = copy.deepcopy(x)
y[1][0] = 0
print(x)
print(y)