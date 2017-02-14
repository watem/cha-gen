import random, importlib, os

classes = input('class? (barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard) ')
lvl = input('lvl? (1-20) ')
#importlib.import_module(classes)










from output import Fname
from output import Lname
os.rename('output.py', '{} {}, {} lvl {}.txt'.format(Fname, Lname, classes, lvl))
