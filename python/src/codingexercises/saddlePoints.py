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