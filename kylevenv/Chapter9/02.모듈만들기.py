import pay_module
# * preference -> setting.json에 extraPath 등록

#변수 사용
print(pay_module.version)

#함수 사용
pay_module.printAuthor()

#클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2022-01-11")
print(pay_info.get_pay_info())

print(pay_module.__name__)