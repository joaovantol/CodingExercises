import heapq

# Goal state and its positions
GOAL_STATE = (1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10,11,12,
              13,14,15,0)

GOAL_POS = {n: (i // 4, i % 4) for i, n in enumerate(GOAL_STATE)}

# Moves and directions
MOVES = {
    'up':    -4,
    'down':   4,
    'left':  -1,
    'right':  1
}

# Check if move is valid
def valid_moves(pos):
    moves = []
    row, col = divmod(pos, 4)
    if row > 0: moves.append('up')
    if row < 3: moves.append('down')
    if col > 0: moves.append('left')
    if col < 3: moves.append('right')
    return moves

# Manhattan distance heuristic
def manhattan(state):
    distance = 0
    for i, val in enumerate(state):
        if val == 0: continue
        goal_r, goal_c = GOAL_POS[val]
        cur_r, cur_c = divmod(i, 4)
        distance += abs(goal_r - cur_r) + abs(goal_c - cur_c)
    return distance

# Apply a move
def move(state, zero_pos, direction):
    new_pos = zero_pos + MOVES[direction]
    state = list(state)
    state[zero_pos], state[new_pos] = state[new_pos], state[zero_pos]
    return tuple(state), new_pos

# A* algorithm
def solve(start_state):
    zero_pos = start_state.index(0)
    frontier = [(manhattan(start_state), 0, start_state, zero_pos, [])]
    seen = set()

    while frontier:
        est_total, cost, state, z, path = heapq.heappop(frontier)

        if state == GOAL_STATE:
            return path

        if state in seen:
            continue
        seen.add(state)

        for direction in valid_moves(z):
            new_state, new_z = move(state, z, direction)
            if new_state in seen:
                continue
            new_cost = cost + 1
            est = new_cost + manhattan(new_state)
            heapq.heappush(frontier, (est, new_cost, new_state, new_z, path + [direction]))

# Initial state
start = (15, 14, 1, 6,
         9, 11, 4, 12,
         0, 10, 7, 3,
         13, 8, 5, 2)

solution = solve(start)
print("Moves:", ', '.join(solution))
print("Move count:", len(solution))