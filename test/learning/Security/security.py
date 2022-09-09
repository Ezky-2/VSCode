import hashlib
import re
import random

def random_string (tedad:int=10):
    from string import ascii_letters
    from random import choice
    return ''.join(choice(ascii_letters) for i in range(tedad))

def hidder(vorodi:str):
    # reverse

    vorodi = re.sub(r'' , ',' , vorodi).split(',')
    vorodi.reverse()

    # replace

    vor = ''
    letter = {
        'a':'d' ,
        'd':'a' ,
        'c':'b' ,
        'b':'c' ,
        'h':'j' ,
        'j':'h' ,
        }
    for har_harf in vorodi:
        if har_harf in letter:
            vor += letter[har_harf]
        else:
            vor += har_harf
    vorodi = vor

    # signture # _!

    return vorodi

def writer(vorodi:str):

    vorodi = hidder(vorodi)

    counter = 0
    e = ''
    random_str = random_string(len(vorodi) + 1)
    for a in vorodi:
        counter += 1
        e = e + str(a) + str(random_str[counter])

    return (e)

def reader(x):
    l = []
    c = 0
    for a in x:
        if c / 2 == c // 2:
            l.append(a)
        c += 1
    l = ''.join(l)

    vorodi = l

    vor = ''
    letter = {
        'a':'d' ,
        'd':'a' ,
        'c':'b' ,
        'b':'c' ,
        'h':'j' ,
        'j':'h' ,
        }
    for har_harf in vorodi:
        if har_harf in letter:
            vor += letter[har_harf]
        else:
            vor += har_harf

    vor = re.sub(r'' , ',' , vor).split(',')
    vor.reverse()

    return ''.join(vor)

x = input('hello: ')
# x = 'hide me'
y = writer(x)
print (y)
print (reader(y))
