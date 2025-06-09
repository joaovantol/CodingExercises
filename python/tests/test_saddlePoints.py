from codingexercises.saddlePoints import saddlePoints

def test_example():
    assert saddlePoints(
    [[9, 8, 7, 8],
     [5, 3, 2, 4],
     [6, 6, 7, 1]]) == [(1, 0)]



# saddlePoints([]) # Empty grid

# saddlePoints(
#     [[9, 8, 7, 8],
#      [5, 3, 2, 4, 2],
#      [6, 6, 7, 1]]
# ) # Irregular grid

# saddlePoints(
#     [[9, 8, 7, 8],
#      [5, 3, 2, 4],
#      [6, 6, 7, 1]]
# ) # [(1, 0)]

# saddlePoints(
#     [[9, 8, 7, 8],
#      [7, 3, 2, 4],
#      [6, 6, 7, 1]]
# ) # No saddle point

# saddlePoints(
#     [[9, 8, 7, 8],
#      [4, 3, 2, 4],
#      [6, 6, 7, 5]]
# ) # [(1, 0), (1, 3)]

