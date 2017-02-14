import random
import importlib

race = ['lightfoot_halfling']
background = ['']

importlib.import_module(random.choice(race))
importlib.import_module(random.choice(background))

archetype_options = ['option1', 'option2']
Archetype = input('archetype? {}, none'.format(archetype_options))


If Archetype is none:
    Archetype = Random.choice(archetype_options)
print(Archetype)

#print(random.choice(a))
