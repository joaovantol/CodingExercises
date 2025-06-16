from codingexercises.spiralMatrix import spiralMatrix

def test_example1():
    assert spiralMatrix(4) == [
        [ 1, 2, 3, 4],
        [12,13,14, 5],
        [11,16,15, 6],
        [10, 9, 8, 7]
    ]

def test_example2():
    assert spiralMatrix(3) == [
        [1,2,3],
        [8,9,4],
        [7,6,5]
    ]
