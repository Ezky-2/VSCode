import mysql.connector
from collections import OrderedDict

Mysql = mysql.connector.connect(user='me' ,
    password='nohack' ,
    database='learning')

curser = Mysql.cursor()

query = 'SELECT * FROM yek;'
curser.execute(query)

l_hh = []
l_ww = []
dict_h = OrderedDict()
dict_w = OrderedDict()
counter = 1
for (n , w , h) in curser:
    if counter == 1:
        first_name = n
    counter += 1
    l_hh.append(h)
    l_ww.append(w)

l_hh.sort(reverse=True)
l_ww.sort()

for har_h in l_hh:
    curser = Mysql.cursor()
    curser.execute(query)
    for (n , w , h) in curser:
        if har_h == h:
            dict_h[n] = h

for har_w in l_ww:
    curser = Mysql.cursor()
    curser.execute(query)
    for (n , w , h) in curser:
        if har_w == w:
            dict_w[n] = w

b = -20
x = first_name
sas = False
counter = 0

for n in dict_h:
    a = dict_h[n]
    if a == b:
        h = dict_w[n]
        g = dict_w[x]
        if h < g:
            print (n , dict_h[n] , dict_w[n])
            print (x , dict_h[x] , dict_w[x])
            sas = True
        else:
            print (x , dict_h[x] , dict_w[x])
    else:
        if not sas:
            if counter != 0:
                print (x , dict_h[x] , dict_w[x])
        else:
            sas = False
    b = a
    x = n
    counter += 1
Mysql.close()
