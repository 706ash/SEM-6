def movegen(current, graph):
    # Returns [child, parent, heuristic]
    return [[n, current, graph[n][1]] for n in graph[current][0]]

def goal_test(current, goals):
    return current in goals

def traversal(closed):
    print("Traversal:", end=" ")
    path = " --> ".join(node[0] for node in closed)
    print(path)

def goal_list_function(graph, mode):
    if mode == 1:
        best_h = min(v[1] for v in graph.values())
    else:
        best_h = max(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1] == best_h]

def steepest_ascent_hill_climbing(graph, mode):
    open_list = []
    closed = []

    start = input("\nEnter the start node: ")
    if start not in graph:
        print("Invalid start node.")
        return

    goal_nodes = goal_list_function(graph, mode)
    open_list.append([start, None, graph[start][1]])

    while open_list:
        # Current is the only element (Hill Climbing is greedy step by step)
        current = open_list.pop(0)
        closed.append(current)

        if goal_test(current[0], goal_nodes):
            print("\nGoal found!")
            traversal(closed)
            return

        neighbors = movegen(current[0], graph)
        if not neighbors:
            break

        fn = min if mode == 1 else max
        best = fn(neighbors, key=lambda x: x[2])

        if (mode == 1 and best[2] >= current[2]) or (mode == 2 and best[2] <= current[2]):
            break

        open_list.append(best)

    print("\nStuck at local optimum.")
    traversal(closed)

def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node, h = input("Enter node and heuristic: ").split()
        neighbors = input(f"Enter neighbours of {node}: ").split()
        graph[node] = [neighbors, int(h)]
    return graph

if __name__ == "__main__":
    graph = input_graph()
    mode = int(input("Enter 1 for minimization or 2 for maximization: "))
    steepest_ascent_hill_climbing(graph, mode)
