prof_str = 'Choi'
prof_tuple = ('Choi', 327, True)
prof_list = ['Choi', 327, True]
prof_set = {'Choi', 327, True}
prof_dict = {'name': 'Choi', 'room_no': 327, 2021: True}

new_str = prof_str + 'Sunglok'
new_list = prof_list + ['Mirae Hall', 'SeoulTech']
prof_set.union({'Mirae Hall', 'SeoulTech'})

print(new_str)
print(new_list)
print(prof_set.union({'Mirae Hall', 'SeoulTech'}))

prof_list.append('Mirae Hall')
prof_set.add('Mirae Hall')
prof_dict['building'] = 'Mirae Hall'

a = not 3.29 > 3 and 10.18 < 10 or 5.12 > 5
b = (not 3.29 > 3) and (10.18 < 10 or 5.12 > 5)
print(a)
print(b)

for i in range(1,4):
    print(i)

print("---------")
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print("---------")

import math
import random
round2 = lambda x: int(x+0.5)
print([round2(random.uniform(0,10)) for i in range(10)])
print([x**2 for x in range(0, 10)])
print(list(map(lambda x: x**2, range(10))))

import fnmatch

profs = ['My name is Choi and my E-mail is sunglok@seoultech.ac.kr.',
'My name is Kim and my e-mail address is jindae.kim@seoultech.ac.kr',
'e-mail ']

print([fnmatch.fnmatch(prof, 'e-mail') for prof in profs])
print([fnmatch.fnmatch(prof, '*e-mail*') for prof in profs])
print([fnmatch.fnmatchcase(prof, '*e-mail*') for prof in profs])
print([fnmatch.fnmatchcase(prof, '*[Ee]-mail*') for prof in profs])

print(fnmatch.filter(profs, '*e-mail*'))
print(fnmatch.filter(profs, '*Ch?i*'))