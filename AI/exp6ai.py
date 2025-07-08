# Water Jug Problem using BFS with rules shown

# Goal: Get exactly 2 gallons in either jug (4-gallon and 3-gallon)

def is_goal(state):
    return state[0] == 2 or state[1] == 2

def get_next_states(state):
    four, three = state
    possible = []

    # Rule 1: Fill 4-gallon jug
    if four < 4:
        possible.append(((4, three), "Fill 4-gallon jug"))

    # Rule 2: Fill 3-gallon jug
    if three < 3:
        possible.append(((four, 3), "Fill 3-gallon jug"))

    # Rule 3: Empty 4-gallon jug
    if four > 0:
        possible.append(((0, three), "Empty 4-gallon jug"))

    # Rule 4: Empty 3-gallon jug
    if three > 0:
        possible.append(((four, 0), "Empty 3-gallon jug"))

    # Rule 5: Pour 4-gallon into 3-gallon jug
    if four > 0 and three < 3:
        total = four + three
        if total > 3:
            possible.append(((total - 3, 3), "Pour 4-gallon into 3-gallon jug"))
        else:
            possible.append(((0, total), "Pour 4-gallon into 3-gallon jug"))

    # Rule 6: Pour 3-gallon into 4-gallon jug
    if three > 0 and four < 4:
        total = four + three
        if total > 4:
            possible.append(((4, total - 4), "Pour 3-gallon into 4-gallon jug"))
        else:
            possible.append(((total, 0), "Pour 3-gallon into 4-gallon jug"))

    return possible

def bfs(start_state):
    queue = []
    visited = []
    queue.append((start_state, []))

    while queue:
        (current_state, path) = queue.pop(0)

        if current_state in visited:
            continue
        visited.append(current_state)

        if is_goal(current_state):
            print_solution(path + [(current_state, "GOAL!")])
            return True

        for (next_state, action) in get_next_states(current_state):
            queue.append((next_state, path + [(current_state, action)]))

    print("No solution found.")
    return False

def print_solution(path):
    print("\nSolution Steps:")
    for idx, (state, action) in enumerate(path):
        if idx == 0:
            print(f"Start State: {state}")
        else:
            print(f"Step {idx}: {action} => State: {state}")
    print("\nAI successfully found a solution!")

if __name__ == "__main__":
    four = int(input("Enter the start state capacity of 4 gallon jar: "))
    three = int(input("Enter the start state capacity of 3 gallon jar: "))
    start_state = (four, three)
    bfs(start_state)
