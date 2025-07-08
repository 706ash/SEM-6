def movegen(current, graph):
    return [[n, graph[n][1]] for n in graph[current][0]]

def goal_test(current, goals):
    return current in goals

def traversal(path):
    print("Traversal:", " --> ".join(path))

def goal_list_function(graph, mode):
    fn = min if mode == 1 else max
    best_h = fn(graph.values(), key=lambda x: x[1])[1]
    return [k for k, v in graph.items() if v[1] == best_h]

def steepest_ascent_hill_climbing(graph, mode):
    start = input("\nEnter the start node: ")
    if start not in graph:
        print("Invalid start node.")
        return

    current = [start, graph[start][1]]
    goal_nodes = goal_list_function(graph, mode)
    path = [start]

    while True:
        if goal_test(current[0], goal_nodes):
            print("\nGoal found")
            traversal(path)
            return

        neighbors = movegen(current[0], graph)
        if not neighbors:
            break

        fn = min if mode == 1 else max
        best = fn(neighbors, key=lambda x: x[1])

        if (mode == 1 and best[1] >= current[1]) or (mode == 2 and best[1] <= current[1]):
            break

        current = best
        path.append(current[0])

    print("\nStuck at local optimum.")
    traversal(path)

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
