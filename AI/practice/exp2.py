def movegen(current, graph):
    return [[n, current] for n in graph[current]]

def goal_test(current, goal):
    return current in goal

def traversal(closed):
    print("\n\nTraversal: ", end="")
    for i in closed:
        print(f"{i[0]} --> ", end=" ")

def bfs(graph):
    open = []
    closed = []

    start_node = input("\n\nEnter the start node: ")
    goal = input("\nEnter the goal node or nodes seperated by spaces: ").split()

    open.append([start_node, None])

    while open:
        current = open[0][0]
        closed.append(open[0])
        del open[0]

        if goal_test(current, goal):
            print("\nGoal found")
            traversal(closed)
            return
        else: 
            child_list = movegen(current, graph)
            for child in child_list:
                if any(child[0] == o[0] for o in open) or any(child[0] == c[0] for c in closed):
                    continue
                open.insert(0, child)

        
    if not goal:
        print("goal not specified")
        return
    else: print("Goal not found")


def input_graph():
    graph = {}
    n = int(input("Enter the no of nodes: "))
    
    for i in range(n):
        node = input("\n\nEnter the node: ")
        neighbours = input(f"Enter the neighbours of the {node} seperated by spaces: ").split()
        graph[node] = neighbours

    return graph    

if __name__ == "__main__":
    graph = input_graph()
    bfs(graph)

