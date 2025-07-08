def get_next_states(state):
    four, three = state
    possible = []

    if four < 4:
        possible.append(((4, three), "Fill the 4 galoon jug completely"))
    
    if three < 3:
        possible.append(((four, 3), "Fill the 3 galoon jug completely"))
    
    if four > 0:
        possible.append(((0, three), "Empty the 4 galoon jug"))

    if three > 0:
        possible.append(((four, 0), "Empty the 3 galoon jug"))

    if four > 0 and three < 3:
        total = four + three
        if total > 3:
            possible.append(((total-3, 3), "Pour water from 4 galoon to 3 galoon"))
        else:
            possible.append(((0, total), "Pour water from 4 galoon to 3 galoon"))

    if three > 0 and four < 4:
        total = four + three
        if total > 4:
            possible.append(((4, total-4), "Pour water from 3 galoon to 4 galoon"))
        else:
            possible.append(((total, 0), "Pour water from 3 galoon to 4 galoon"))

    return possible

def goal_test(state):
    return state[0] == 2 or state[1] == 2

def print_goal(path):
    print("Solution steps: ")
    for idx, (state, action) in enumerate(path):
        if idx == 0:
            print(f"Start state:{action} => {state}")
        else:
            print(f"Step {idx}: {action} => {state}")
    
    print("AI succesfully found a solution")

def bfs(start_state):
    queue = []
    visited = []
    queue.append((start_state, []))

    while queue:
        (current_state, path) = queue.pop(0)

        if current_state in visited:
            continue
        visited.append(current_state)

        if goal_test(current_state):
            print_goal(path + [(current_state, "GOAL STATE")])
            return True
        
        for (next_state, action) in get_next_states(current_state):
            queue.append((next_state, path + [(current_state, action)]))
        
    print("No solution found")
    return False
        

if __name__ == "__main__":
    four = int(input("Enter the initial water in the 4 galoon jug: "))
    three = int(input("Enter the initial water in the 3 galoon jug: "))

    start_state = (four, three)
    bfs(start_state)