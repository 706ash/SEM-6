def movegen(current, graph):
    return [[n, graph[n][1]] for n in graph[current][0]]


def goal_test(current, goal):   
    return current in goal


def traversal(path):
    print("Traversal ", end="")
    for i in range(len(path)):
        print(path[i], end=" ")
        if i != len(path) - 1: 
            print("-->", end=" ")
    print()


def goal_list_function(graph, a):
    if a == 1:
        goal_node_heuristic = min(graph.values(), key=lambda x: x[1])[1]
    else:
        goal_node_heuristic = max(graph.values(), key=lambda x: x[1])[1]

    goal_nodes = [k for k, v in graph.items() if v[1] == goal_node_heuristic]    
    return goal_nodes


def steepest_ascent_hill_climbing(graph, a):
    start_node = input("\n\nEnter the start node: ")
    goal_nodes = goal_list_function(graph, a)
    
    try:
        current = [start_node, graph[start_node][1]]
    except KeyError:
        print("\nError! Please enter a valid start node...")
        exit()
    
    path = [start_node]
    
    while True:
        if goal_test(current[0], goal_nodes):
            print("\n\nGoal found\n")
            traversal(path)
            return
            
        neighbors = movegen(current[0], graph)
        if not neighbors:  # If no neighbors exist
            break
            
        # Find the best neighbor
        best_neighbor = min(neighbors, key=lambda x: x[1]) if a == 1 else max(neighbors, key=lambda x: x[1])
        
        # Check if we're stuck
        if (a == 1 and best_neighbor[1] >= current[1]) or (a == 2 and best_neighbor[1] <= current[1]):
            break
            
        current = best_neighbor
        path.append(current[0])
    
    print("\n\nStuck at local maximum/minimum. Terminating search.")
    traversal(path)


def input_graph():
    graph = {}
    
    graph = {
    "A": [["B", "C"], 1],
    "B": [["D"], 2],
    "C": [["R", "S"], 4],
    "D": [[], 7],
    "R": [[], 50],
    "S": [[], 12]
    }
    print("Enter the number of nodes:", len(graph))
    print()

    for node, value in graph.items():
        neighbors = value[0]
        heuristic = value[1]
        
        print(f"Enter a node and its heuristic value separated by spaces: {node} {heuristic}")
        if neighbors:
            print(f"Enter the neighbors of {node} separated by spaces: {' '.join(neighbors)}")
        else:
            print(f"Enter the neighbors of {node} separated by spaces: ")
        print()
    
    
    # MINIMIZATION GRAPH
    

    # MAXIMIZATION GRAPH
    

    

        
    return graph


if __name__ == "__main__":
    graph = input_graph()
    a = int(input("\n\nEnter 1 for minimization and 2 for maximization: "))
    steepest_ascent_hill_climbing(graph, a)
    print()
