from codingexercises.coinCombinations import coinCombinations

def test_1():
    assert coinCombinations(1) == 1

def test_2():
    assert coinCombinations(2) == 2

def test_3():
    assert coinCombinations(3) == 2

def test_4():
    assert coinCombinations(4) == 3

def test_5():
    assert coinCombinations(5) == 4
