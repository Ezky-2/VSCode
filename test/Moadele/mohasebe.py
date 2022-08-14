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

# print (mosavi('(13 + 11)*1*(5 + 6)' , '200 + 60 + 4'))

Run()
