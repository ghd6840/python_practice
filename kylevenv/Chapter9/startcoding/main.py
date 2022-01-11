# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈
from unit import item
item.test()

# 3. from 패키지 import *  (*을 쓰기위해선 init 모듈을 설정해야한다.)
from unit import *
character.test()
item.test()
monster.test()

# 4. import 패키지  (똑같이 init모듈에 설정이 필요)
import unit
unit.character.test()
unit.item.test()
unit.monster.test()