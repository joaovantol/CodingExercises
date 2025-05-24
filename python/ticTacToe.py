def isRowWinner(field):
    turnsX = field.count("X")
    turnsO = field.count("O")
    if abs(turnsX - turnsO) > 1:
        return False, "Invalid field"

    winnerX = False
    winnerO = False

    for row in range(3):
        start = row * 3
        line = field[start:start+3]
        
        if line[0] == line[1] == line[2] == "X":
            winnerX = True
        if line[0] == line[1] == line[2] == "O":
            winnerO = True
        
    if winnerX and winnerO:
        return False, "Invalid field"
    elif winnerX:
        return True, "X wins"
    elif winnerO:
        return True, "O wins"
    else:
        return False, "No winner"
    
isRowWinner(['X', 'X', 'X', 'O', 'O', '.', '.', '.', '.']) # X wins
isRowWinner(['X', 'O', 'X', 'O', 'O', 'O', 'X', '.', 'X']) # O wins
isRowWinner(['X', 'O', '.', '.', 'X', 'O', '.', '.', 'X']) # no winner
isRowWinner(['X', 'X', 'X', 'O', 'O', 'O', '.', '.', '.']) # invalid field (both X and Y wins)
isRowWinner(['X', 'X', 'X', 'X', 'X', 'O', '.', '.', '.']) # invalid field (X taken 5 turns and O taken 1 turn)
