# append
countries = ['Korea', 'Japan', 'China']
country = 'France'
countries.append(country)

print(countries)

# pop(), pop(index)
countries.pop()
print(countries)

countries.pop(0)
print(countries)

# del
del(countries[1])
print(countries)

# remove
countries.remove('Japan')
print(countries)

# index -> find index
countries.append(country)
countries.append('Brazil')
print(countries)

# count -> specific value count
count = countries.count('France')
print(count)

# clear -> remove all
countries.clear()
print(countries)

# sort
numbers = [2, 3, 1, 7, 5, 4]
numbers.sort()
print(numbers)

# enumerate
# for in 사용시 print index
subjects = ['Math', 'English', 'Science', 'Social']

for index, subject in enumerate(subjects): #enumerate(subjects, 1) <- start index value
    print(index+1, subject) #print(index, subject)
    print(f'{index+1} 번째 과목은 {subject} 입니다.')
