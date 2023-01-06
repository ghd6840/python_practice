# if no 문자열 포맷팅
name = 'Kyle'
time = 10

message = name + '님 PC 사용시간이 ' + str(time) + ' 남았습니다.'
print(message)

# if use 문자열 포맷팅
message_with_format = f'{name}님 PC 사용시간이 {time} 남았습니다.'
print(message_with_format)

# format method
a = 'Hello {0}{1}{2}'.format('Korea','Japan','China')
print(a)

b = 'Hello {} {} {}'.format('Korea', 'Japan', 'China')
print(b)

# f-string
country1 = 'Korea'
country2 = 'Japan'
country3 = 'China'

c = f'Thank you for visiting ASIA {country1}, {country2}, {country3}'
print(c)
