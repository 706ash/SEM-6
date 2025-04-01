graph = {}
is_maximization = False

def add_edges(vertex, neighbors):
    graph[vertex] = neighbors

def steepest_hill_climbing(source, heuristic):
    path, traversal, cost = [source], [source], heuristic[source]
    global_optimum = max(heuristic.values()) if is_maximization else min(heuristic.values())

    while True:
        neighbors = graph.get(source, [])
        if not neighbors:
            break

        sorted_neighbors = sorted(neighbors, key=lambda node: heuristic[node], reverse=is_maximization)
        next_node = sorted_neighbors[0] if sorted_neighbors else None
        
        if not next_node or (is_maximization and heuristic[next_node] <= heuristic[source]) or (not is_maximization and heuristic[next_node] >= heuristic[source]):
            break

        # Check for plateau
        if len(sorted_neighbors) > 1 and heuristic[sorted_neighbors[0]] == heuristic[sorted_neighbors[1]]:
            print("Plateau Detected")
            break
        
        source, cost = next_node, cost + heuristic[next_node]
        path.append(source)
        traversal.append(source)
    
    print("Reached Local Optimum")
    print("Path taken:", " -> ".join(path))
    print("Traversal of the Graph:", " -> ".join(traversal))
    print(f"Total Traversal Cost: {cost}")
    
    # Classification
    if heuristic[path[-1]] == global_optimum:
        print("Global Optimum Reached")
    else:
        print("Local Optimum Reached")
    
    if path[0] == path[-1]:
        print("Initial node is the Goal node")
    
    if heuristic[path[-1]] > global_optimum and not is_maximization:
        print("Overestimation of heuristic values detected")
    if heuristic[path[-1]] < global_optimum and is_maximization:
        print("Underestimation of heuristic values detected")

def get_input():
    global is_maximization
    is_maximization = input("Is this a maximization or minimization problem? (max/min): ").strip().lower() == "max"
    
    for _ in range(int(input("Enter the number of vertices: "))):
        vertex = input("Vertex: ").strip()
        add_edges(vertex, input(f"Enter neighbors of {vertex} (space-separated): ").strip().split())
    
    heuristic = {v: int(input(f"Enter heuristic for {v}: ")) for v in graph}
    steepest_hill_climbing(input("Enter the source node: ").strip(), heuristic)

get_input()
