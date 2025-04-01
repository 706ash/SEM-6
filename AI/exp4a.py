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
    
    # graph = {
    # "A": [["B", "C"], 50],
    # "B": [["D", "E"], 40],
    # "C": [["F"], 30],
    # "D": [[], 45],
    # "E": [[], 20],
    # "F": [[], 25]
    # }

    # graph = {
    # "A": [["B"], 5],   # Node A has child B and heuristic value 5
    # "B": [["C"], 4],   # Node B has child C and heuristic value 4
    # "C": [["D"], 3],   # Node C has child D and heuristic value 3
    # "D": [["E"], 2],   # Node D has child E and heuristic value 2
    # "E": [[], 1]     # Node E has no children and heuristic value 1
    # }

    # graph = {
    # "A": [["B", "C"], 3],  # Node A has children B and C, and heuristic value 3
    # "B": [[], 3],          # Node B has no children and heuristic value 3
    # "C": [[], 3]           # Node C has no children and heuristic value 3
    # }

    # graph = {
    # "A": [["B", "C"], 2],  # Node A has children B and C, and heuristic value 2
    # "B": [["C"], 3],       # Node B has child C and heuristic value 3
    # "C": [[], 4]          # Node C has no children and heuristic value 4
    # }

    # graph = {
    # "A": [["B", "C"], 5],  # Node A has children B and C, and heuristic value 5
    # "B": [[], 6],          # Node B has no children and heuristic value 6
    # "C": [["D"], 4],       # Node C has child D and heuristic value 4
    # "D": [[], 5]          # Node D has no children and heuristic value 5
    # }
    
    # graph = {
    # "A": [["B", "C"], 5],  # Node A has children B and C, and heuristic value 5
    # "B": [["D"], 2],       # Node B has child D and heuristic value 2
    # "D": [[], 1],          # Node D has no children and heuristic value 1
    # "C": [[], 4]           # Node C has no children and heuristic value 4
    # }

    # graph = {
    # "A": [["B", "C"], 5],  # Node A has children B and C, and heuristic value 5
    # "B": [["D"], 6],       # Node B has child D and heuristic value 6
    # "C": [["E"], 7],       # Node C has child E and heuristic value 7
    # "E": [[], 7]           # Node E has no children and heuristic value 7
    # }

    # graph = {
    # "A": [["B", "C"], 10],  # Start node
    # "B": [["D", "E"], 15],  # Local maximum
    # "C": [["F"], 12],  
    # "D": [[], 17],  # A better path but not reachable from local max
    # "E": [[], 14],  
    # "F": [["G"], 20],  # Global maximum (should be reached but isn't)
    # "G": [[], 25]  # Best state
    # }

    # graph = {
    # "A": [["B", "C"], 50],  # Start node
    # "B": [["D", "E"], 30],  # Leads to a plateau
    # "C": [["F"], 40],  
    # "D": [["G", "H"], 20],  # All have the same heuristic (plateau)
    # "E": [["I"], 20],  
    # "F": [["J"], 25],  
    # "G": [[], 20],  # Plateau
    # "H": [[], 20],  # Plateau
    # "I": [["K"], 10],  # The actual best path
    # "J": [[], 15],  
    # "K": [[], 5]  # Global minimum (not reached)
    # }

    # graph = {
    # "A": [["B", "C"], 10],  # Start node
    # "B": [["D"], 15],  
    # "C": [["E"], 20],  
    # "D": [[], 25],  # Intermediate high value
    # "E": [["G"], 30],  # Higher than D
    # "G": [[], 40]  # Goal node (Global Maximum)
    # }

    # graph = {
    # "A": [["B", "C"], 10],  # Start node
    # "B": [["D", "E"], 20],  # Plateau begins
    # "C": [["F"], 15],  
    # "D": [["G"], 20],  # Plateau (same heuristic as B and E)
    # "E": [["H"], 20],  # Plateau
    # "F": [[], 18],  
    # "G": [[], 20],  # Plateau
    # "H": [[], 20]  # Plateau
    # }

    # graph = {
    # "A": [["B", "C"], 10],  # Start node
    # "B": [["D"], 20],  # Plateau begins
    # "C": [["E"], 15],  
    # "D": [[], 20],  # Plateau (same heuristic as B)
    # "E": [[], 25]   # Better option, but unreachable
    # }

    # graph = {
    # "A": [["B"], 10],  # Node A has child B and heuristic value 10
    # "B": [[], 9]       # Node B has no children and heuristic value 9
    # }

    # graph = {
    # "A": [["B", "C"], 15],  # Node A has children B, C and heuristic value 15
    # "B": [["D"], 12],       # Node B has child D and heuristic value 12
    # "C": [["E"], 10],       # Node C has child E and heuristic value 10
    # "D": [[], 8],           # Node D has no children and heuristic value 8
    # "E": [[], 5]            # Node E has no children and heuristic value 5
    # }

    graph = {
    "A": [["B", "C"], 2],   # Node A has children B, C and heuristic value 2
    "B": [["D"], 3],        # Node B has child D and heuristic value 3
    "C": [["E"], 1],        # Node C has child E and heuristic value 1
    "D": [[], 0],           # Node D has no children and heuristic value 0
    "E": [[], 0]            # Node E has no children and heuristic value 0
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
