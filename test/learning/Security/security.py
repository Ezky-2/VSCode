import hashlib

def writer(vorodi):
    y = hashlib.sha512(vorodi.encode()).hexdigest()
    t2 = hashlib.sha512(vorodi.encode()).hexdigest()
    y = y + t2
    counter = 0
    e = ''

    for a in vorodi:
        counter += 1
        e = e + str(a) + str(y[counter])

    print ('\n' , e)
    return (e)

def reader(x):
    l = []
    c = 0
    for a in x:
        if c / 2 == c // 2:
            l.append(a)
        c += 1

    print (''.join(l) , '\n')

x = input('hello: ')
y = writer(x)
reader(y)
