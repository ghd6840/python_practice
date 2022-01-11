#모듈을 사용하는 이유
# - 프로그램 기능별로 파일을 나누어서 유지보수 등 관리를 편하게 하기 위해 사용.

#모듈의 개념
# - 한개의 완성된 프로그램 파일

#파이썬 기본(내장) 모듈 사용방법
# import 모듈이름   
# 모듈이름.변수      
# 모듈이름.함수()

import math
print(math.pi)
print(math.ceil(5.7))

from math import pi,ceil
print(pi)
print(ceil(5.7))

from math import pi, ceil as up
print(up(2.6))

#파이썬 외부 모듈 사용방법
# pip install 모듈이름  pip install pyautogui  -- 매크로 관련 모듈

import pyautogui as pg

pg.moveTo(1000,1000, duration=2)
