def movegen(current, graph):
    return [[n, current] for n in graph[current]]

def traversal(closed):
    path = "  -->  ".join(c[0] for c in closed)
    print(f"Traversal: {path}")


def goal_test(current, goal):
    return current in goal


def bfs(graph):
    open, closed = [], []

    start = input("Enter the start node: ")
    goal_nodes = input("enter the goal node or nodes sep by spaces: ").split()

    open.append([start, None])

    while open:
        current = open[0][0]
        closed.append(open[0])
        del open[0]

        if goal_test(current, goal_nodes):
            print("Goal found")
            traversal(closed)
            return
        else:
            child_nodes = movegen(current, graph)
            for child in child_nodes:
                if any(child[0] == n[0] for n in open + closed):
                    continue
                open.append(child)
    
    if not goal_nodes:
        print("Goal not specified")
    else:
        print("Goal not found")

def input_graph():
    graph = {}
    n = int(input("Enter the no of nodes in the graph: "))

    for _ in range(n):
        node = input("Enter the node: ")
        neighbours = input(f"Enter the neighbours of {node} sepeaterd ny spaces: ").split()
        graph[node] = neighbours
    
    return graph

if __name__ == "__main__":
    graph = input_graph()
    bfs(graph)