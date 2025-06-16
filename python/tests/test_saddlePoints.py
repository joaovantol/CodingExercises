from pytest import raises
from codingexercises.saddlePoints import saddlePoints

def test_1():
    assert saddlePoints(
    [[9, 8, 7, 8],
     [5, 3, 2, 4],
     [6, 6, 7, 1]]) == [(1, 0)]

def test_2():
    assert saddlePoints(
    [[9, 8, 7, 8],
     [7, 3, 2, 4],
     [6, 6, 7, 1]]) == []

def test_3():
    assert saddlePoints(
    [[9, 8, 7, 8],
     [4, 3, 2, 4],
     [6, 6, 7, 5]]) == [(1, 0), (1, 3)]

def test_4():
    with raises(ValueError, match = "Empty grid"):
        saddlePoints([])

def test_5():
    with raises(ValueError, match = "Irregular grid"):
        saddlePoints([
            [9, 8, 7, 8],
            [5, 3, 2, 4, 2],
            [6, 6, 7, 1]])
