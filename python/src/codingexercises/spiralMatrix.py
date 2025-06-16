def spiralMatrix(dim):
    matrix = [[0] * dim for _ in range(dim)]
    row, col, drow, dcol = 0, 0, 0, 1

    for matrix[row][col] in range(1, dim * dim + 1):
        row, col = row + drow, col + dcol
        nextRow, nextCol = row + drow, col + dcol
        if nextRow >= dim or nextCol >= dim or nextCol < 0 or matrix[nextRow][nextCol]:
            drow, dcol = dcol, -drow

    return matrix