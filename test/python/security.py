def writer(x):
    import hashlib
    t = x.encode()
    y = hashlib.sha512(t).hexdigest()
    t2 = hashlib.sha512(t).hexdigest()
    y = y + t2
    counter = 0
    e = ''
    for a in x:
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
reader(x)

