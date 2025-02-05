def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]


def goal_test(current, goal):   
    return current in goal


def traversal(closed):
    print("Traversal ", end="")

    for i in range(len(closed)):
        print(closed[i][0], end=" ")
        if i != len(closed) - 1: 
            print("-->", end=" ")
  
    
def goal_list_function(graph):
    goal_node_heuristic = min(graph.values())[1]
    goal_nodes = [k for k, v in graph.items() if v[1] == goal_node_heuristic]    
    return goal_nodes
    
def dfs(graph):
    open = []
    closed = []
    
    start_node = input("\n\nEnter the start node: ")
    goal_node = goal_list_function(graph)
    
    open.append([start_node,None,graph[start_node][1]])
    
    while open:   
        min,index = open[0],0
        
        for i in range(1, len(open)):
            if open[i][2] < min[2]:
                index = i
                min = open[i]
                   
        closed.append(min)
        del open[index]
        
        if goal_test(min[0], goal_node):
            print("\n\nGoal found\n")
            traversal(closed)
            return                    
        else:
            child_list = movegen(min[0], graph)
            for child in child_list:
                if any(child[0] == o[0] for o in open) or any(child[0] == c[0] for c in closed):
                    continue
                open.insert(0, child)
            
            
    
    if not goal_node:
        print("\n\nGoal node not specified")
        traversal(closed)
    else:print("\n\nGoal not found")
            
            
def input_graph():
    graph = {
    'A': [['B', 'C', 'D'], 6],  
    'B': [['E', 'F'], 4],  
    'C': [['G', 'H'], 4],  # Same heuristic as B  
    'D': [['I'], 5],  
    'E': [[], 3],  
    'F': [['J'], 2],  
    'G': [[], 3],  
    'H': [['K'], 2],  # Same heuristic as F  
    'I': [[], 4],  
    'J': [[], 1],  # Goal node  
    'K': [[], 1]   # Another goal node  
    }



    # n = int(input("Enter the number of nodes: "))
    
    # for i in range(n):
    #     pair = input("Enter a node and it's heuristic value seperated by spaces: ").split()
    #     neighbours = input(f"Enter the neighbours of {pair[0]} seperated by spaces: ").split()
    #     graph[pair[0]] = [neighbours,int(pair[1])]
    # print(graph)
    return graph


if __name__ == "__main__":
    graph = input_graph()
    dfs(graph)
    print()