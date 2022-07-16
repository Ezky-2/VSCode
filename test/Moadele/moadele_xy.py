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

def mazrab_harf_ha (vorodi): # برای گذاشتن ضرب پشت مجهول ها
    x = re.findall(r'\d+\w' , vorodi)
    for har_moshkel in x:
        a = re.findall(r'\d+' , har_moshkel)[0]
        b = re.findall(r'\d+(\w)' , har_moshkel)[0]
        vorodi = re.sub(a+b , a+'*'+b , vorodi)
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
    return n1 + n2

def tafrigh (n1 , n2):
    return n1 - n2

def zarb (n1 , n2):
    return n1 * n2

def taghsim (n1 , n2):
    return n1 / n2

def tavan (n1 , n2):
    return n1 ** n2

def mohasebe (vorodi , alamat):
    return (alamat(int(vorodi[0]) , int(vorodi[1])))

def last_tavan (vorodi):
    x = re.findall(r'(\d+)\s*\*\*\s*(\d+)' , vorodi)
    x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , tavan)
    vorodi = re.sub(r'%s\s*\*\*\s*%s' %(x[0] , x[1]) , str(y) , vorodi)

    return vorodi

def last_zarb (vorodi):
    x = re.findall(r'(\d+)\s*\*\s*(\d+)' , vorodi)
    x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , zarb)
    vorodi = re.sub(r'%s\s*\*\s*%s' %(x[0] , x[1]) , str(y) , vorodi)
    return vorodi

def last_taghsim_1 (vorodi):
    x = re.findall(r'(\d+)\s*\\\\\s*(\d+)' , vorodi)
    x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , taghsim)
    vorodi = re.sub(r'%s\s*\\\\\s*%s' %(x[0] , x[1]) , str(y) , vorodi)

    return vorodi

def last_taghsim_2 (vorodi):
    x = re.findall(r'(\d+)\s*\/\s*(\d+)' , vorodi)
    x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , taghsim)
    vorodi = re.sub(r'%s\s*\/\s*%s' %(x[0] , x[1]) , str(y) , vorodi)

    return vorodi

def last_jam (vorodi):
    x = re.findall(r'(\d+)\s*\+\s*(\d+)' , vorodi)
    if x == []:
        return vorodi
    else:
        x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , jam)
    vorodi = re.sub(r'%s\s*\+\s*%s' %(x[0] , x[1]) , str(y) , vorodi)

    return vorodi

def last_tafrigh (vorodi):
    x = re.findall(r'(\d+)\s*\-\s*(\d+)' , vorodi)
    if x == []:
        return vorodi
    else:
        x = x[0]
    y = mohasebe( [ int (x [0]) , int (x [1]) ] , tafrigh)
    vorodi = re.sub(r'%s\s*\-\s*%s' %(x[0] , x[1]) , str(y) , vorodi)

    return vorodi

def mosavi_helper (vorodi):
    import re
    list_alamat_ha = list()

    # برای پیدا کردن علامت های ورودی
    list_alamat_ha_ba_space = re.findall(r'\D' , vorodi)
    for har_alamat in list_alamat_ha_ba_space:
        if har_alamat != ' ':
            list_alamat_ha.append(har_alamat)

    for har_alamat in list_alamat_ha:
        if har_alamat == '*' or har_alamat == '\\' or har_alamat == '/':
            if har_alamat == '*':
                vorodi = last_zarb(vorodi)
            elif har_alamat == '\\':
                vorodi = last_taghsim_1(vorodi)
            elif har_alamat == '/':
                vorodi = last_taghsim_2(vorodi)

    for har_alamat in list_alamat_ha:
        if har_alamat == '-' or har_alamat == '+':
            if har_alamat == '-':
                vorodi = last_tafrigh(vorodi)
            if har_alamat == '+':
                vorodi = last_jam(vorodi)

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

    paian_1 = float(paian_1)
    paian_2 = float(paian_2)


    if paian_1 == paian_2:
        return [True  , paian_1 , paian_2]
    else:
        return [False , paian_1 , paian_2]

def moadele(vorodi:str , vorodi_range_1 , vorodi_range_2):
    
    vorodi_h = vorodi
    vorodi = vorodi.split('=')
    vorodi_1 = mazrab_harf_ha(parantez(vorodi[0]))
    vorodi_2 = mazrab_harf_ha(parantez(vorodi[1]))

    my_dict = OrderedDict()

    for x in range(1,vorodi_range_1):
        for y in range(1,vorodi_range_2):

            a = jaigozari(vorodi_1 , x , y , vorodi_h)
            b = jaigozari(vorodi_2 , x , y , vorodi_h)

            paian = mosavi(a , b)[0] # برسی مساوی بودن دو طرف معادله
            if paian:
                my_dict[x] = y # اضافه کردن اعداد صحیح به لیست برای نشان دادن

    harf = re.findall(r'([a-zA-Z])' , vorodi_h)

    if my_dict != OrderedDict():
        return my_dict , harf

    else:
        return 'No Math'

# توی ران همه چی هست خودت رابط بساز

def Run(vorodi:str=False , vorodi_range_1:int=10 , vorodi_range_2:int=10 , returnable=False):

    # گرفتن ورودی و تجزیه آن
    if not vorodi:
        vorodi = input('Enter your moadele: ')

    if vorodi == 'exit':
        exit()
    if vorodi == '':
        return 'Please enter something'

    if returnable:
        return moadele(vorodi , vorodi_range_1 , vorodi_range_2)
    else:
        print (moadele(vorodi , vorodi_range_1 , vorodi_range_2)[0])

# Run()
