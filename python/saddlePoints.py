def saddlePoints(grid):
    if not grid:
        raise ValueError("Empty grid")
    
    if len(set([len(row) for row in grid])) != 1:
        raise ValueError("Irregular grid")
    
    cols = list(zip(*grid))
    saddlePoints = []
    
    for rowIndex, row in enumerate(grid):
        for colIndex, value in enumerate(row):
            if (value == max(row) and value == min(cols[colIndex])):
                saddlePoints.append((rowIndex, colIndex))
    
    return saddlePoints




saddlePoints([]) # Empty grid

saddlePoints(
    [[9, 8, 7, 8],
     [5, 3, 2, 4, 2],
     [6, 6, 7, 1]]
) # Irregular grid

saddlePoints(
    [[9, 8, 7, 8],
     [5, 3, 2, 4],
     [6, 6, 7, 1]]
) # [(1, 0)]

saddlePoints(
    [[9, 8, 7, 8],
     [7, 3, 2, 4],
     [6, 6, 7, 1]]
) # No saddle point

saddlePoints(
    [[9, 8, 7, 8],
     [4, 3, 2, 4],
     [6, 6, 7, 5]]
) # [(1, 0), (1, 3)]
