def mineCounter(board):
    rows = len(board)
    cols = len(board[0])
    countedBoard = []

    for row in range(rows):
        countedRow = ""
        for col in range(cols):
            if board[row][col] == "*":
                countedRow += "*"
            else:
                count = 0
                for drow in [-1, 0, 1]:
                    for dcol in [-1, 0, 1]:
                        if drow == dcol == 0:
                            continue
                        checkrow, checkcol = row + drow, col + dcol
                        if 0 <= checkrow < rows and 0 <= checkcol < cols:
                            if board[checkrow][checkcol] == "*":
                                count += 1
                countedRow += str(count) if count > 0 else " "
        countedBoard.append(countedRow)

    return countedBoard


board1 = [" * * ",
         "  *  ",
         "  *  ",
         "     "]
mineCounter(board1)

board2 = [" * *    * ",
          "  *      *",
          "        **",
          "     *   *",
          "    **    ",
          "          ",
          "    *   **",
          "   *      ",
          " *        ",
          "     * *  "]
mineCounter(board2)
for line in mineCounter(board2):
    print(line)