import re

vorodi = '32 + 12x = -10 y-2'

x = re.findall(r'\d+\w' , vorodi)
for har_moshkel in x:
    a = re.findall(r'\d+' , har_moshkel)[0]
    b = re.findall(r'\d+(\w)' , har_moshkel)[0]
    vorodi = re.sub(a+b , a+'*'+b , vorodi)
# x = re.sub(r'\d+\w' , vorodi)
print (x , vorodi)
