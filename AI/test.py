def goal_list_function():
    graph = {
        'S': [['A', 'B', 'C'], -1],
        'A': [['D','E'], 2],
        'B': [['F','G'], 6],
        'C': [['H'], 5],
        'D': [[], 10],
        'E': [[], 8],
        'F': [[], 10],
        'G': [[], 14],
        'H': [['I'], 7],
        'I': [['K', 'L', 'M'], 5],
        'K': [[], 1],
        'L': [[], 0],
        'M': [[], 2],
    }
    goal_node_heuristic = min(graph.values(), key = lambda x: x[1])[1]
    print(goal_node_heuristic)
    goal_nodes = [k for k, v in graph.items() if v[1] == goal_node_heuristic]    
    return goal_nodes


print(goal_list_function())