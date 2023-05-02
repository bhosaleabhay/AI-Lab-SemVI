from collections import deque

def bfs_tower_of_hanoi(num_disks):
    # Initialize the starting state and the goal state
    start_state = (tuple(range(num_disks, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(num_disks, 0, -1)))

    # Initialize the queue with the starting state
    queue = deque([start_state])

    # Initialize an empty set to store the visited states
    visited = set()

    # Initialize an empty dictionary to store the parent of each state
    parents = {}

    # Loop until the queue is empty or the goal state is found
    while queue:
        # Dequeue the first state in the queue
        current_state = queue.popleft()

        # If the current state is the goal state, return the optimal path
        if current_state == goal_state:
            # Initialize an empty list to store the optimal path
            path = []

            # Trace back from the goal state to the starting state using the parents dictionary
            while current_state != start_state:
                path.append(current_state)
                current_state = parents[current_state]

            # Append the starting state to the path and reverse it
            path.append(start_state)
            path.reverse()

            # Return the path
            return path

        # Add the current state to the visited set
        visited.add(current_state)

        # Get the valid moves from the current state
        valid_moves = get_valid_moves(current_state)

        # Loop through each valid move
        for move in valid_moves:
            # Generate the next state by applying the move
            next_state = apply_move(current_state, move)

            # If the next state has not been visited yet, add it to the queue and the parent dictionary
            if next_state not in visited:
                queue.append(next_state)
                parents[next_state] = current_state

    # If the goal state is not found, return None
    return None


def get_valid_moves(state):
    # Get the positions of the top disks on each peg
    top_disks = [peg[-1] if peg else float('inf') for peg in state]

    # Initialize an empty list to store the valid moves
    valid_moves = []

    # Loop through each peg
    for i in range(len(state)):
        # Loop through each other peg
        for j in range(len(state)):
            if i != j:
                # If the top disk on peg i can be moved to peg j, add the move to the valid moves list
                if top_disks[i] < top_disks[j]:
                    valid_moves.append((i, j))

    # Return the valid moves list
    return valid_moves


def apply_move(state, move):
    # Get the source and destination pegs from the move tuple
    src, dst = move

    # Get the lists of disks on the source and destination pegs from the state tuple
    src_list, dst_list = list(state[src]), list(state[dst])

    # Remove the top disk from the source peg and add it to the destination peg
    dst_list.append(src_list.pop())

    # Create a new state tuple with the updated peg lists
    new_state = list(state)
    new_state[src] = tuple(src_list)
    new_state[dst] = tuple(dst_list)

    # Return the new state tuple
    return tuple(new_state)

def main():
    num_disks = 3
    optimal_path = bfs_tower_of_hanoi(num_disks)
    if optimal_path:
        print(f"Optimal Path for {num_disks} disks:\n")
        for state in optimal_path:
            print_state(state)
            print()
    else:
        print(f"No solution found for {num_disks} disks.")

def print_state(state):
    for peg in state:
        print(peg)
    print("-----")

if __name__ == '__main__':
    main()