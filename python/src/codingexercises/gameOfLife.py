def neighbors(board: list[list[int]], i: int, j: int) -> list[tuple[int, int]]:
    """
    Get all valid neighboring positions (including diagonals) for a given cell.

    Args:
        board: The game board (2D list)
        i: Row index of the cell
        j: Column index of the cell

    Returns:
        list of valid (row, col) neighbor positions within board bounds
    """
    n = len(board)
    all_neighbors = [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),               (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]
    return [(x, y) for (x, y) in all_neighbors if 0 <= x < n and 0 <= y < n]

def tick(board: list[list[int]]) -> list[list[int]]:
    """
    Compute the next generation of the Game of Life.

    Args:
        board: Current game state (2D list where 1=alive, 0=dead)

    Returns:
        New game state after one iteration
    """
    n = len(board)
    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            live_count = sum(1 for x, y in neighbors(board, i, j) if board[x][y] == 1)

            if board[i][j] == 1:
                if live_count == 2 or live_count == 3:
                    new_board[i][j] = 1
            else:
                if live_count == 3:
                    new_board[i][j] = 1

    return new_board
