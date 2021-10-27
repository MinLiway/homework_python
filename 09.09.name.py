import string
s=string.ascii_lowercase

import random
vowel=['a','b', 'c']
cons=['d','f', 'g']
ln=['sun','claud', 'rain']
def generation_name(vowel,cons,num):
    i=1
    while i<num:
        name=''
        name+=random.choice(ln)+' '
        for x in range(0, 3):
            name+=random.choice(cons)
            name+=random.choice(vowel)
        yield name
        i+=1
for name in generation_name(vowel,cons,5):
    print(name)
