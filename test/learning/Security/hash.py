from hashlib import sha256
import re

def hash_lib (file):

    # read hash file
    with open(file , 'r') as vorodi:
        hashs = []
        vorodi = vorodi.readlines()
        for har_hash in vorodi:
            hashs.append(re.sub(r'\,' , '' ,re.sub(r'\s*' , '' , har_hash)))

    # create possible hash and password
    hash_pass = dict()
    for har_adad in range(0,1001):
        hash_adad = sha256(str(har_adad).encode()).hexdigest()
        hash_pass[hash_adad] = har_adad

    for har_vorodi in hashs:
        if har_vorodi in hash_pass:
            print (har_vorodi , hash_pass[har_vorodi])

hash_lib('/home/Erfan/VSCode/VSCode/test/learning/Security/hash.csv')


















# 536326188b56c7f1da0345518c1eca5f5c97cc6d958611fe17cee6fb0fa989bc,
# c789a815d8bba2a356562d89f62b98993932fda1533a916cfcd47adbfe39967b,
# 7bf3c227f531b4cd730604d5b5317698aff98d84c250406dbc621c2fc29dd8ec,
# 9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0,
# 377ac4e989ab213e6cb678957fb78f6ba9c41a84e2d2e10fb972d36143e7d192,
