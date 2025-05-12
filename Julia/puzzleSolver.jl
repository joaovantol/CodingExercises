using Pkg
Pkg.add("DataStructures")

using DataStructures

const GOAL = [1, 2, 3, 4,
              5, 6, 7, 8,
              9,10,11,12,
             13,14,15, 0]

# Map of goal positions
const GOAL_POS = Dict(GOAL[i] => ((i - 1) ÷ 4, (i - 1) % 4) for i in 1:16)

# Valid directions
const DIRS = Dict("up" => -4, "down" => 4, "left" => -1, "right" => 1)

function manhattan(state::Vector{Int})
    dist = 0
    for i in 1:16
        val = state[i]
        if val == 0
            continue
        end
        goal_r, goal_c = GOAL_POS[val]
        cur_r, cur_c = (i - 1) ÷ 4, (i - 1) % 4
        dist += abs(goal_r - cur_r) + abs(goal_c - cur_c)
    end
    return dist
end

function valid_moves(pos::Int)
    row, col = (pos - 1) ÷ 4, (pos - 1) % 4
    moves = String[]
    if row > 0; push!(moves, "up"); end
    if row < 3; push!(moves, "down"); end
    if col > 0; push!(moves, "left"); end
    if col < 3; push!(moves, "right"); end
    return moves
end

function apply_move(state::Vector{Int}, zero_pos::Int, direction::String)
    new_pos = zero_pos + DIRS[direction]
    new_state = copy(state)
    new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
    return new_state, new_pos
end

function solve(start::Vector{Int})
    zero_pos = findfirst(==(0), start)
    seen = Set{Vector{Int}}()
    frontier = PriorityQueue{Tuple{Vector{Int}, Int, Vector{String}}, Int}()

    enqueue!(frontier, (start, zero_pos, String[]), manhattan(start))

    while !isempty(frontier)
        state, zpos, path = dequeue!(frontier)

        if state == GOAL
            return path
        end

        if state in seen
            continue
        end
        push!(seen, state)

        for dir in valid_moves(zpos)
            new_state, new_z = apply_move(state, zpos, dir)
            if new_state in seen
                continue
            end
            new_path = copy(path)
            push!(new_path, dir)
            cost = length(new_path) + manhattan(new_state)
            enqueue!(frontier, (new_state, new_z, new_path), cost)
        end
    end
    return nothing
end

# Initial configuration
initial = [15,14, 1, 6,
            9,11, 4,12,
            0,10, 7, 3,
           13, 8, 5, 2]

# Solve the puzzle
solution = solve(initial)

if solution !== nothing
    println("Moves: ", join(solution, ", "))
    println("Move count: ", length(solution))
else
    println("No solution found.")
end


function print_board(state::Vector{Int})
    println()
    for i in 1:4:13
        row = state[i:i+3]
        println(join([x == 0 ? "  " : lpad(x, 2) for x in row], " "))
    end
end



if solution !== nothing
    println("Solution found in ", length(solution), " moves.")
    println("Moves: ", join(solution, ", "))
    
    # Replay the board step-by-step
    current = copy(initial)
    zpos = findfirst(==(0), current)
    
    println("\nInitial State:")
    print_board(current)

    for (i, move) in enumerate(solution)
        current, zpos = apply_move(current, zpos, move)
        println("\nStep $i: $move")
        print_board(current)
    end

    println("\nSolved!")
else
    println("No solution found.")
end