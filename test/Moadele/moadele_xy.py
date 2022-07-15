# + - * /

from collections import OrderedDict
import re

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

def jam (n1 , n2):
    return n1 - (- n2)

def tafrigh (n1 , n2):
    return n1 + (~n2 + 1)

def zarb (n1 , n2):
    mul = 0
    if n2 < 0:
        n2 = -n2
        n1 = -n1
    for i in range(1 , n2 + 1):
        mul = mul + n1
    return mul

def taghsim (n1 , n2):
    neg = False
    peg = 0

    if n1 == 0 or n2 == 0:
        return 0
    
    if n1 < 0:
        n1 = -n1
        neg = True
        if n2 < 0:
            n2 = -n2
            neg = False

    if n2 < 0:
        n2 = -n2
        neg = True
        if n1 < 0:
            n1 = -n1
            neg = False

    while n1 >= n2:
        n1 -= n2
        peg += 1

    if neg:
        peg = -peg
    return peg

def tavan (n1 , n2):
    sho = n1
    neg = False

    if n1 == 0 and n2 == 0:
        return 0
    if n1 == 0 or n2 == 0:
        return 1

    if n1 < 0:
        n1 = -n1
        neg = True
        if n2 < 0:
            n2 = -n2
            neg = False

    if n2 < 0:
        n2 = -n2
        neg = True
        if n1 < 0:
            n1 = -n1
            neg = False

    for a in range(1,n2):
        sho = sho * n1
    
    if neg:
        sho = -sho
    return sho

def mohasebe (vorodi , alamat):
    return (alamat(int(vorodi[0]) , int(vorodi[1])))

def mosavi_helper (vorodi):
    import re

    while '**' in vorodi:
        x = re.findall(r'(\d+)\s*\*\*\s*(\d+)' , vorodi)
        x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , tavan)
        vorodi = re.sub(r'\d+\s*\*\*\s*\d+' , str(y) , vorodi)

    while '*' in vorodi:
        x = re.findall(r'(\d+)\s*\*\s*(\d+)' , vorodi)
        x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , zarb)
        vorodi = re.sub(r'\d+\s*\*\s*\d+' , str(y) , vorodi)

    while '\\' in vorodi:
        x = re.findall(r'(\d+)\s*\\\\\s*(\d+)' , vorodi)
        x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , taghsim)
        vorodi = re.sub(r'\d+\s*\\\\\s*\d+' , str(y) , vorodi)

    while '/' in vorodi:
        x = re.findall(r'(\d+)\s*\/\s*(\d+)' , vorodi)
        x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , taghsim)
        vorodi = re.sub(r'\d+\s*\/\s*\d+' , str(y) , vorodi)

    while '+' in vorodi:
        x = re.findall(r'(\d+)\s*\+\s*(\d+)' , vorodi)
        if x == []:
            break
        else:
            x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , jam)
        vorodi = re.sub(r'\d+\s*\+\s*\d+' , str(y) , vorodi)

    while '-' in vorodi:
        x = re.findall(r'(\d+)\s*\-\s*(\d+)' , vorodi)
        if x == []:
            break
        else:
            x = x[0]
        y = mohasebe( [ int (x [0]) , int (x [1]) ] , tafrigh)
        vorodi = re.sub(r'\d+\s*\-\s*\d+' , str(y) , vorodi)

    return vorodi

def parantezs (vorodi):
    import re

    while True:
        in_parantez = re.search(r'\((.+?)\)' , vorodi)

        if in_parantez == None:
            break
        else:
            x = in_parantez[0]
            adad = mosavi_helper(x)
            adad = re.findall(r'\d+' , adad)[0]
            vorodi = re.sub(r'\(.+?\)' , str(adad) , vorodi , 1)

    return mosavi_helper (vorodi)

def mosavi (vorodi_aval , vorodi_dovom):
    import re

    parantez_sang_1 = re.search(r'\(.+\)' , vorodi_aval)
    parantez_sang_2 = re.search(r'\(.+\)' , vorodi_dovom)

    # طرف اول
    if parantez_sang_1 == None:
        paian_1 = mosavi_helper(vorodi_aval)
    else:
        paian_1 = parantezs(vorodi_aval)

    # طرف دوم
    if parantez_sang_2 == None:
        paian_2 = mosavi_helper(vorodi_dovom)
    else:
        paian_2 = parantezs(vorodi_dovom)

    paian_1 = int(paian_1)
    paian_2 = int(paian_2)

    if paian_1 == paian_2:
        return [True  , paian_1 , paian_2]
    else:
        return [False , paian_1 , paian_2]

def Run():
    vorodi = input('Enter your moadele: ')
    vorodi = vorodi.split('=')
    TOF = mosavi(vorodi[0] , vorodi[1])
    if TOF[0]:
        print (TOF[1] , '=' , TOF[2])
    else:
        if TOF[1] > TOF[2]:
            print (TOF[1] , '>' , TOF[2])
        elif TOF[1] < TOF[2]:
            print (TOF[1] , '<' , TOF[2])
        else:
            print ('chi?')

def moadele(vorodi:str):

    # گرفتن ورودی و تجزیه آن
    if vorodi == 'exit':
        exit()
    if vorodi == '':
        return 'Please enter something'

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
                return x , y
                # my_dict[x] = y # اضافه کردن اعداد صحیح به لیست برای نشان دادن

    # harf = re.findall(r'([a-zA-Z])' , vorodi_h)
    # print (harf)

    # از اینجا بنویس

    # if my_dict != OrderedDict():
    #     for har_OK in my_dict: # نوشتن اعداد درست
    #         print ('%s is %i  and  %s is %i' % (harf[0] , har_OK , harf[1] , my_dict[har_OK]))

    # else:
    #     print ('No Math')

print(moadele('x-(2+4)+3=y-(5+0)'))
