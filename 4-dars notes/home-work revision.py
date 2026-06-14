my_list = [10, 20, 30, 20, 40]

index = my_list.index(20)
qwerty = my_list[1]
print(index)  # 1
print(qwerty)  # 1

print("-"*50)
from collections import defaultdict
# person = {
#     'name' : 'Ali',
#     'age' : 7
# }

# email = person.get('email')
# if not email:
#     email = 'No email'

# print(email)

# person = defaultdict(list)
person = {}
person['name'] = 'Ali'
person.setdefault('skills', [])
person['skills'].append('python')
person['skills'].append('gooning')
person['skills'].append('writing')

print(person['skills'])

