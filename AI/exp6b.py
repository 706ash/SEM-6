import random
from collections import deque

state_space = {
    (0, 0): [((4, 0), 1), ((0, 3), 2)],
    (1, 0): [((0, 0), 3), ((4, 0), 1), ((1, 3), 2), ((0, 1), 6)],
    (2, 0): [((0, 0), 3), ((4, 0), 1), ((2, 3), 2), ((0, 2), 6)],
    (3, 0): [((0, 0), 3), ((4, 0), 1), ((3, 3), 2), ((0, 3), 6)],
    (4, 0): [((0, 0), 3), ((4, 3), 2), ((1, 3), 6)],
    (0, 1): [((4, 1), 1), ((0, 0), 3), ((0, 3), 2), ((1, 0), 5)],
    (0, 2): [((4, 2), 1), ((0, 0), 3), ((0, 3), 2), ((2, 0), 5)],
    (0, 3): [((4, 3), 1), ((0, 0), 3), ((3, 0), 5)],
    (1, 1): [((0, 1), 3), ((4, 1), 1), ((1, 0), 3), ((2, 0), 5), ((0, 2), 6)],
    (2, 1): [((0, 1), 3), ((4, 1), 1), ((2, 0), 3), ((3, 0), 5), ((0, 3), 6)],
    (3, 1): [((0, 1), 3), ((4, 1), 1), ((3, 0), 3), ((4, 0), 5), ((1, 3), 6)],
    (4, 1): [((0, 1), 3), ((4, 0), 4), ((4, 3), 2), ((2, 3), 6)],
    (1, 2): [((0, 2), 3), ((4, 2), 1), ((1, 0), 3), ((3, 0), 5), ((0, 3), 6)],
    (1, 3): [((0, 3), 3), ((4, 3), 1), ((1, 0), 3), ((4, 0), 5)],
    (2, 2): [((0, 2), 3), ((4, 2), 1), ((2, 0), 4), ((4, 0), 5), ((1, 3), 6)],
    (3, 2): [((0, 2), 3), ((4, 2), 1), ((3, 0), 4), ((4, 1), 5), ((2, 3), 6)],
    (4, 2): [((0, 2), 3), ((4, 3), 2), ((4, 0), 4), ((3, 3), 6)],
    (2, 3): [((0, 3), 3), ((4, 3), 1), ((2, 0), 4), ((4, 1), 5)],
    (3, 3): [((0, 3), 3), ((4, 3), 1), ((3, 0), 4), ((4, 2), 5)],
    (4, 3): [((0, 3), 3), ((4, 0), 4)],
}

rule_base = {
    1: "Fill 4-gallon jug",
    2: "Fill 3-gallon jug",
    3: "Empty 4-gallon jug",
    4: "Empty 3-gallon jug",
    5: "Pour 3-gallon jug into 4-gallon jug",
    6: "Pour 4-gallon jug into 3-gallon jug"
}


def img(fourg, threeg, rule, open_list, closed_list):
    print("------------------------")
    print(f"Current State: ({fourg}, {threeg})")
    if rule:
        print(f"Applied Rule: {rule_base[rule]}")
    print(f"Open List: {[state for state, _, _ in open_list]}")
    print(f"Closed List: {closed_list}")
    print("|  |      ")
    print("|  |  |  |")
    print("|  |  |  |")
    print(f"({fourg}) , ({threeg})")


def main():
    goal_input = input("Enter the goal state (e.g., 2,3): ")
    goal = tuple(map(int, goal_input.strip().split(",")))

    open_list = deque()
    open_list.append(((0, 0), None, []))  # (state, rule applied, path)
    closed_list = []

    while open_list:
        current, applied_rule, path = open_list.popleft()
        img(current[0], current[1], applied_rule, open_list, closed_list)

        if current == goal:
            print("\nGoal reached!")
            print("Path to goal:")
            for step in path + [(current, applied_rule)]:
                if step[1]:
                    print(f"{step[0]} via {rule_base[step[1]]}")
                else:
                    print(f"{step[0]} (start)")
            return

        if current in closed_list:
            continue

        closed_list.append(current)

        for child_state, rule in state_space.get(current, []):
            if child_state not in closed_list:
                open_list.append((child_state, rule, path + [(current, applied_rule)]))

    print("No path found to goal!")


main()
