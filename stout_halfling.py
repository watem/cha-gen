import random
#import importlib

race = 'stout_halfling'

sexs = ['Male', 'Female']
name_firstM = ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich', 'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo', 'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby']
name_firstF = ['Andry', 'Bree', 'Callie', 'Cora', 'Euphemia', 'Jillian', 'Kithri', 'Lavinia', 'Lidda', 'Merla', 'Nedda', 'Paela', 'Portia', 'Seraphina', 'Shaena', 'Trym', 'Vani', 'Verna']
name_last = ['Brushgather', 'Goodbarrel', 'Greenbottle', 'High-hill', 'Hilltopple', 'Leagallow', 'Tealeaf', 'Thorngage', 'Tosscobble', 'Underbough']
size = 'small'
speed = '25ft'
race_traits = ['lucky', 'brave', 'halfling nimbleness', 'stout resilience']






sex = random.choice(sexs)
if sex is 'Male':
    name_first = name_firstM
else:
    name_first = name_firstF

file = open('output.py', 'w')

file.write('race = \'{}\' \n'.format(race))
file.write('sex = \'{}\' \n'.format(sex))
file.write('Fname = \'{}\' \n'.format(random.choice(name_first)))
file.write('Lname = \'{}\' \n'.format(random.choice(name_last)))
file.write('features = {} \n'.format(race_traits))


#file.write('[object] = \'{}\' \n'.format(object))
#file.write('[list] = {} \n'.format(list))
file.close()
