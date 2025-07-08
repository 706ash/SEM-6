def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]


def traversal(closed):
    path = "  -->  ".join(c[0] for c in closed)
    print(f"Traversal: {path}")


def goal_test(current, goal):
    return current in goal

def glf(graph, mode):
    if mode == 1:
        min_h = min(v[1] for v in graph.values())
    else:
        min_h = max(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1]==min_h]

def bfs(graph, mode):
    open, closed = [], []
    start = input("Enter the start node: ")
    if start not in graph:
        print("Error")
    goal_nodes = glf(graph, mode)

    open.append([start, None, graph[start][1]])

    while open:
        current = open.pop(0)
        closed.append(current)

        if goal_test(current[0], goal_nodes):
            print("Goal found")
            traversal(closed)
            return
            
        neighbours = movegen(current[0], graph)
        if not neighbours:
            break
        fn = min if mode == 1 else max
        best = fn(neighbours, key=lambda x:x[2])

        if (mode ==1 and best[2] >= current[2]) or (mode ==2 and best[2] <= current[2]):
            break
        open.append(best)

    print("Local optimum reached")

def input_graph():
    graph = {}
    n = int(input("Enter the no of nodes: "))

    for _ in range(n):
        node, h = input("Enter node and heuristic: ").split()
        neighbours = input(f"Enter neighbours of {node}: ").split()
        graph[node] = [neighbours, int(h)]
     
    return graph

if __name__ == "__main__":
    graph = input_graph()
    mode = int(input("Enter 1 for minimization and 2 for maximization"))
    bfs(graph, mode)
