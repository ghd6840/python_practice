#6.1.3
#로또에 당첨돼서 퇴사를 하고싶었던 김로또는 로또예상번호 추출 프로그램을 파이썬으로 작성하려고한다.
#다음 조건에 따라 김로또의 프로그램을 완성해보자
# 1. 로또 번호 6개를 생성한다.
# 2. 로또번호는 1~45까지의 랜덤한 번호다.
# 3. 6개의 숫자 모두 달라야한다.
# 4. getRandomNumber() 함수를 사용해서 구현한다. (random 모듈의 sample 함수는 사용하지 않는다.)

import random
def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto = []
count = 0

while True:
    if count > 5:
        break

    random_number = getRandomNumber()

    if random_number not in lotto:
        lotto.append(random_number)
        count += 1

lotto.sort()
for num in lotto:
    print(num, end=" ")

#번호 중복 신경안쓸경우
test_lotto = []
for i in range(6):
    ran_number = getRandomNumber()
    test_lotto.append(ran_number)

test_lotto.sort()
print(test_lotto)
