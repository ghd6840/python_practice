# positional variable length parameter 위치 가변 매개변수
# 매개변수 앞에 *가 붙음(튜플형) args
def print_fruits(*args):
    print(args)

print_fruits('apple', 'orange', 'grape', 'peach')


# keyword variable length parameter 키워드 가변 매개변수
# 매개변수 앞에 **가 붙음(딕셔너리형) kwargs
def comment_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

comment_info(name='kyle', content='Nice to meet you')


# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(*tags, title, content):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')

post_info('#python','#angular',title = 'languages',content = 'select project language')

def post_info(title, content, *tags):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')

post_info('languages', 'lecture content', '#python', 'parameter')