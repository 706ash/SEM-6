def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]

def traversal(closed):
    path = '  -->  '.join(c[0] for c in closed)
    print(f"Traversal: {path}")

def goal_list_fn(graph):
    min_h = min(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1] == min_h]
 
def goal_test(current, goal):
    return current in goal

def best_first_search(graph):
    open_list, closed = [], []

    start = input("Enter the start node: ")
    goal_nodes = goal_list_fn(graph)

    if start not in graph:
        print("Start node is not in graph")
        return

    open_list.append([start, None, graph[start][1]])

    while open_list:
        current = min(open_list, key = lambda x: x[2])
        closed.append(current)
        open_list.remove(current)

        if goal_test(current[0], goal_nodes):
            print("Goal Found")
            traversal(closed)
            return

        for child in movegen(current[0], graph):
            if any(child[0] == n[0] for n in open_list + closed):
                continue
            open_list.append(child)

    print("Goal not found...")

def input_graph():
    graph = {}
    n = int(input("Enter the no of nodes: "))

    for _ in range(n):
        node, h = input("Enter the node and its heuristic seperated by spaces: ").split()
        neighbours = input(f"Enter the neighbours of {node} seperated by spaces: ").split()
        graph[node] = [neighbours, int(h)]
    
    print(graph)
    return graph

if __name__ == "__main__":
    graph = input_graph()
    best_first_search(graph)