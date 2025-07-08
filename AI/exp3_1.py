def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]

def goal_test(current, goals):
    return current in goals

def traversal(closed):
    path = " --> ".join(node[0] for node in closed)
    print(f"Traversal {path}")

def goal_list_function(graph):
    min_h = min(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1] == min_h]

def dfs(graph):
    open_list, closed = [], []
    start = input("\nEnter the start node: ")
    goals = goal_list_function(graph)

    if start not in graph:
        print("Invalid start node.")
        return

    open_list.append([start, None, graph[start][1]])

    while open_list:
        current = min(open_list, key=lambda x: x[2])
        closed.append(current)
        open_list.remove(current)

        if goal_test(current[0], goals):
            print("\nGoal found!\n")
            traversal(closed)
            return

        for child in movegen(current[0], graph):
            if any(child[0] == n[0] for n in open_list + closed):
                continue
            open_list.append(child)

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node, h = input("Enter node and heuristic: ").split()
        neighbours = input(f"Enter neighbours of {node}: ").split()
        graph[node] = [neighbours, int(h)]
    return graph

if __name__ == "__main__":
    graph = input_graph()
    dfs(graph)
    print()
