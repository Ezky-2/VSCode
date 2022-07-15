def func(x):
    if x == 4:
        return 4
    return x + 2

def test_one():
    assert func(3) == 5

def test_two():
    assert func(4) == 6

def test_three():
    assert func(5) == 2