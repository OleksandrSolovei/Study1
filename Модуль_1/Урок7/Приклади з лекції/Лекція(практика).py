my_str = '''finally
dungeon
bleakly
grouchy
rigidly
whether
startle
neglect
gaseous
grenade
whoever
noisily
merrily
beatify
dimpled
limping
hospice
phooey
gaseous
boohoo
blocker
uh-huh
amusing
buoyant
wearily
barring
whether
instead
briskly
washtub
sternly
pronoun
phooey
whether
despite
prickle
bathtub
amongst
trumpet
merrily
finally
huzzah
monocle
heavily
educate
testify
bargain
bleakly
vicious
promote
excited
however
beneath
briskly
rations
culture
swiftly
lyocell
catcher
between
gadzooks
frankly
huzzah
earnest
however
frankly
instead
spatter
warm-up
because
because
uh-huh
despite
because
monthly
against
therapy
shallow
huzzah
despite
dogsled
needily
pungent
oddball
barring
whereas
finally
without
spanish
whoever
poleaxe
happily
knowing
jaywalk
boycott
granola
whether
opening
astride
thrifty'''
my_list = my_str.split()
print(my_list)
my_dict = dict()
for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
print(my_dict)
