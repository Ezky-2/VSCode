from moadele_xy import *

def test_one():
    x = 'x = y'
    assert moadele(x) == (1, 1)

def test_two():
    x = ''
    assert moadele(x) == 'Please enter something'

def test_three():
    x = '10 +3+ x=y -9'
    assert moadele(x) == (1, 23)

def test_four():
    x = 'x/2 = y/3'
    assert moadele(x) == (1, 3)

def test_five():
    x = 'a-(2+4)+3=b-(5+0)'
    assert moadele(x) == (3, 5)

