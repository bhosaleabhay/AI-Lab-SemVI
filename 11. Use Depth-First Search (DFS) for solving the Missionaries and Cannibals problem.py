from collections import deque

class State:
    def __init__(self, m_left, c_left, m_right, c_right, boat_side):
        self.m_left = m_left
        self.c_left = c_left
        self.m_right = m_right
        self.c_right = c_right
        self.boat_side = boat_side
        self.parent = None

    def is_valid(self):
        if self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
            return False
        if self.m_left != 0 and self.m_left < self.c_left:
            return False
        if self.m_right != 0 and self.m_right < self.c_right:
            return False
        return True

    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0

    def __eq__(self, other):
        return self.m_left == other.m_left and self.c_left == other.c_left and \
               self.m_right == other.m_right and self.c_right == other.c_right and \
               self.boat_side == other.boat_side

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.m_right, self.c_right, self.boat_side))

    def __str__(self):
        return f"State({self.m_left}, {self.c_left}, {self.m_right}, {self.c_right}, {self.boat_side})"

def successors(state):
    children = []
    if state.boat_side == 'left':
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(state.m_left - m, state.c_left - c, state.m_right + m, state.c_right + c, 'right')
                    if new_state.is_valid():
                        new_state.parent = state
                        children.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    new_state = State(state.m_left + m, state.c_left + c, state.m_right - m, state.c_right - c, 'left')
                    if new_state.is_valid():
                        new_state.parent = state
                        children.append(new_state)
    return children

def dfs(start_state):
    visited, stack = set(), [start_state]
    while stack:
        state = stack.pop()
        if state.is_goal():
            path = []
            while state.parent:
                path.append(state)
                state = state.parent
            path.append(state)
            path.reverse()
            return path
        visited.add(state)
        for child in successors(state):
            if child not in visited:
                stack.append(child)

start_state = State(3, 3, 0, 0, 'left')
path = dfs(start_state)
for state in path:
    print(state)
