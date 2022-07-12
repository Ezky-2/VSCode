import re
from mosavi import mosavi_helper

vorodi_aval = '5 + 7*(76 + 45) + 5 + (76) + 65'

    in_parantez = re.findall(r'\((.+?)\)' , vorodi_aval)
    if in_parantez == []:
        break
    for a in in_parantez:
        adad = mosavi_helper(a)
        l.append(adad)
    x = re.search(r'\(.+?\)' vorodi_aval)
print (vorodi_aval)