def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]


def traversal(closed):
    path = "  -->  ".join(c[0] for c in closed)
    print(f"Traversal: {path}")


def goal_test(current, goal):
    return current in goal

def glf(graph):
    min_h = min(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1]==min_h]

def bfs(graph):
    open, closed = [], []
    start = input("Enter the start node: ")
    if start not in graph:
        print("Error")
    goal_nodes = glf(graph)

    open.append([start, None, graph[start][1]])

    while open:
        current = min(open, key = lambda x:x[2])
        closed.append(current)
        open.remove(current)

        if goal_test(current[0], goal_nodes):
            print("Goal found")
            traversal(closed)
            return
        for child in movegen(current[0], graph):
            if any(child[0] == n[0] for n in open + closed):
                continue
            open.append(child)

    print("goal not found")

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
    bfs(graph)
