from queue import PriorityQueue

# Define the problem
initial_state = (3, 3, 1)   # (left_m, left_c, boat)
goal_state = (0, 0, 0)      # (right_m, right_c, boat)

# Define the heuristic function (admissible and consistent)
def heuristic(state):
    return state[0] + state[1]

# Define the cost function
def cost(prev_state, next_state):
    return 1

# Define the function to get next states
def get_next_states(state):
    next_states = []
    if state[2] == 1:   # boat is on the left side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2 and state[0] >= i and state[1] >= j:
                    next_states.append((state[0] - i, state[1] - j, 0))
    else:   # boat is on the right side
        for i in range(3):
            for j in range(3):
                if i + j > 0 and i + j <= 2 and 3 - state[0] >= i and 3 - state[1] >= j:
                    next_states.append((state[0] + i, state[1] + j, 1))
    return next_states

# Define the A* Search algorithm
def a_star(initial_state, goal_state, heuristic, cost, get_next_states):
    frontier = PriorityQueue()
    frontier.put((0 + heuristic(initial_state), 0, initial_state))
    explored = set()
    came_from = {}
    came_from[initial_state] = None
    while not frontier.empty():
        _, g, current_state = frontier.get()
        if current_state == goal_state:
            path = [current_state]
            while path[-1] != initial_state:
                path.append(came_from[path[-1]])
            path.reverse()
            return path
        explored.add(current_state)
        for next_state in get_next_states(current_state):
            new_g = g + cost(current_state, next_state)
            new_h = heuristic(next_state)
            new_f = new_g + new_h
            if next_state not in explored:
                frontier.put((new_f, new_g, next_state))
                came_from[next_state] = current_state
    return None

# Run the algorithm and print the solution
path = a_star(initial_state, goal_state, heuristic, cost, get_next_states)
if path is not None:
    print("Steps to reach the goal:")
    for state in path:
        print(state)
        print("-----------")
else:
    print("No solution found.")