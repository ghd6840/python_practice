# 리스트 내포를 사용해서 word_list에 들어있는 문자열 중 첫글자가 a인것만 뽑아서 리스트를 만드세요.
word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']

# without 리스트 내포
result = []
for word in word_list:
    if word[0] == 'a':
        result.append(word)
print(result)

# with 리스트 내포
result2 = [i for i in word_list if i[0] == 'a']
print(result2)


# 리스트 내포를 사용해서 다음과 같이 변경해보자
# ['오메가3',None,'비타민C',None,'비타민B'] => ['오메가3','','비타민C','','비타민B']

items = ['오메가3',None,'비타민C',None,'비타민B']
result3 = []
# without 리스트 내포
for item in items:
    if item != None:
        result3.append(item)
    else:
        result3.append('')

print(result3)

#with 리스트 내포
result4 = [i if i != None else '' for i in items]
print(result4)
