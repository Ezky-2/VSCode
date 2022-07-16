from moadele_xy import *

def test_one ():
    x = 'x = y'
    assert Run(x , returnable=True) == (1, 1)

def test_two ():
    x = ''
    assert Run(x , returnable=True) == 'Please enter something'
    pass

def test_three ():
    x = '10 +3+ x=y -9'
    assert Run(x , returnable=True) == (1 , 23)

def test_four ():
    x = 'x/2 = y/3'
    assert Run(x , returnable=True) == (2 , 3)

def test_five ():
    x = 'a-(2+4)+3=b-3'
    assert Run(x , returnable=True) == (6 , 6)

def test_six ():
    x = '2x+1=2y-1'
    assert Run(x , returnable=True) == (1 , 2)

def test_seven ():
    x = '3X - 4Y =   1'
    assert Run(x , returnable=True) == (3 , 2)

def test_eghit ():
    x = '2x - x = y - 4'
    assert Run(x , returnable=True) == (1 , 5)