# positional parameter - 위치 매개변수

def my_func(a,b):
    print(a,b)

my_func('python','study')

# default parameter - 기본 매개변수

def post_info(title, content):
    print('제목 : ', title)
    print('내용 : ', content)

post_info('title', '')

# Keyword parameter - 키워드 매개변수
# 매개변수 순서 지키지 않아도 됨

def post_info(title, content):
    print('제목 : ', title)
    print('내용 : ', content)

post_info(content='내용', title='제목')