from collections import namedtuple


# NewPerson = namedtuple('NewPerson', 'name, race, health, mana, strength')
# hero = NewPerson('Ooz', 'Ozoretane', 100.0, 0.0, 150)
# print(hero.name, hero.race, sep='\n')
#
# prop = ['name', '3race', 'health', '_mana', 'strength']
# NewPerson_1 = namedtuple('NewPerson_1', prop, rename=True)
# hero1 = NewPerson_1('Wookie', 'Ozoretane', 100.0, 0.0, 450)
# print(hero1)

Point = namedtuple('Point', 'x, y, z')

p1 = Point(3, z=12.1, y=5.9)
print(p1)

t = ['2.0', '3.4', '1.2']
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
"""
bpo-35864: The _asdict() method for collections.namedtuple now returns a regular dict instead of an OrderedDict.
"""
print(d2)

p3 = p2._replace(y=11)
print(p3)
print(p3._fields)

print('=' * 30)

NewPoint = namedtuple('NewPoint', 'x, y, z', defaults=[0, 0])
p4 = NewPoint(13)
print(p4)
print(p4._field_defaults)

dc = {'x': 4.0, 'y': 3.1, 'z': 0.5}
p5 = Point(**dc)
print(p5)
