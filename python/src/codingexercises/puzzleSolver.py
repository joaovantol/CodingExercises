import heapq

def validMoves(pos):
    moves = []
    row, col = divmod(pos, 4)
    if row > 0: moves.append('up')
    if row < 3: moves.append('down')
    if col > 0: moves.append('left')
    if col < 3: moves.append('right')
    return moves

def manhattan(state, goalPositions):
    distance = 0
    for i, val in enumerate(state):
        if val == 0: continue
        goalRow, goalCol = goalPositions[val]
        currentRow, currentCol = divmod(i, 4)
        distance += abs(goalRow - currentRow) + abs(goalCol - currentCol)
    return distance

def move(state, zeroPos, moves, direction):
    newPos = zeroPos + moves[direction]
    state = list(state)
    state[zeroPos], state[newPos] = state[newPos], state[zeroPos]
    return tuple(state), newPos

def solve(startState, goalState):
    goalPositions = {n: (i // 4, i % 4) for i, n in enumerate(goalState)}

    moves = {'up':    -4,
             'down':   4,
             'left':  -1,
             'right':  1}

    zeroPos = startState.index(0)
    frontier = [(manhattan(startState, goalPositions), 0, startState, zeroPos, [])]
    seen = set()

    while frontier:
        estTotal, cost, state, z, path = heapq.heappop(frontier)

        if state == goalState:
            return path

        if state in seen:
            continue
        seen.add(state)

        for direction in validMoves(z):
            newState, newZ = move(state, z, moves, direction)
            if newState in seen:
                continue
            newCost = cost + 1
            est = newCost + manhattan(newState, goalPositions)
            heapq.heappush(frontier, (est, newCost, newState, newZ, path + [direction]))

startState = (15, 14, 1, 6,
              9, 11, 4, 12,
              0, 10, 7, 3,
              13, 8, 5, 2)

goalState = (1, 2, 3, 4,
             5, 6, 7, 8,
             9, 10,11,12,
             13,14,15,0)

solution = solve(startState, goalState)
print("Moves:", ', '.join(solution))
print("Move count:", len(solution))









