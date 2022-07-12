# + - * /

def parantez (vorodi): # برای گذاشتن ضرب بین پرانتز ها
    vorodi = vorodi.replace(')(' , ')*(')
    vorodi = vorodi.replace(') (' , ')*(')

    x = re.search(r'\w+\s*\(' , vorodi)
    if x != None:
        y = re.search(r'\w+' , x.group())
        vorodi = re.sub(r'\w+\s*\(' , y.group() + '*' + '(' , vorodi)

    x = re.search(r'\)\s*\w+' , vorodi)
    if x != None:
        y = re.search(r'\w+' , x.group())
        vorodi = re.sub(r'\)\s*\w+' ,  ')'  + '*' + y.group() , vorodi)
    
    return vorodi

def harf_ha_def (vorodi): # برای پیدا کردن مجهول ها مثل x , y | a ,b 
    l = []
    x = (re.findall(r'([a-zA-Z])' , vorodi))
    for a in x:
        if a not in l:
            l.append(a)
    return l

def jaigozari (vorodi , adad_1 , adad_2 , vorodi_harf):

    adad_1 = str(adad_1)
    adad_2 = str(adad_2)

    harf_sang = True
    harf = re.findall(r'([a-zA-Z])' , vorodi)
    if harf == []:
        return vorodi
    l_harf = harf_ha_def(vorodi_harf)
    true = vorodi

    while harf_sang:
        if harf == [] or harf == None:
            harf_sang = False
            continue
        x = harf[0]
        if x == l_harf[0]:
            adad = adad_1
        elif x == l_harf[1]:
            adad = adad_2
        else:
            adad = 'Error in jaigozari'

        true = re.sub(x , adad , true)
        harf = re.findall(r'([a-zA-Z])' , true)

    return true

# مقدار دهی و import کردن

from mohasebe import mosavi
from collections import OrderedDict
import re

vorodi = None
while vorodi != 'exit':

    # گرفتن ورودی و تجزیه آن

    vorodi = input('Enter your moadele: ')

    if vorodi == '':
        print ('Enter something')
        continue
    vorodi_h = vorodi
    vorodi = vorodi.split('=')
    vorodi_1 = vorodi[0]
    vorodi_2 = vorodi[1]

    vorodi_1 = parantez(vorodi_1)
    vorodi_2 = parantez(vorodi_2)

    vorodi_range_1 = 100
    vorodi_range_2 = 100

    # start

    my_dict = OrderedDict()

    for x in range(1,vorodi_range_1):
        for y in range(1,vorodi_range_2):

            a = jaigozari(vorodi_1 , x , y , vorodi_h)
            b = jaigozari(vorodi_2 , x , y , vorodi_h)

            paian = mosavi(a , b)[0] # برسی مساوی بودن دو طرف معادله
            if paian:
                my_dict[x] = y # اضافه کردن اعداد صحیح به لیست برای نشان دادن

    harf = re.findall(r'([a-zA-Z])' , vorodi_h)
    print (harf)
    if my_dict != OrderedDict():
        for har_OK in my_dict: # نوشتن اعداد درست
            print ('x is %i  and  y is %i' % (har_OK , my_dict[har_OK]))

    else:
        print ('No Math')

