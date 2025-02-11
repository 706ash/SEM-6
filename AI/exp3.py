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
    goal_node_heuristic = min(graph.values(), key = lambda x: x[1])[1]
    goal_nodes = [k for k, v in graph.items() if v[1] == goal_node_heuristic]    
    return goal_nodes
    
def dfs(graph):
    open = []
    closed = []
    
    start_node = input("\n\nEnter the start node: ")
    goal_node = goal_list_function(graph)
    
    try:
        open.append([start_node,None,graph[start_node][1]])
    except:
        print("\nError! Please enter a start node...")
        exit()
    
    while open:   
        #fetch the min node from the open list
        minimum = min(open, key = lambda x: x[2])
                   
        closed.append(minimum)
        del open[open.index(minimum)]
        
        if goal_test(minimum[0], goal_node):
            print("\n\nGoal found\n")
            traversal(closed)
            return                    
        else:
            child_list = movegen(minimum[0], graph)
            for child in child_list:
                if any(child[0] == o[0] for o in open) or any(child[0] == c[0] for c in closed):
                    continue
                open.insert(0, child)
            

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    for i in range(n):
        pair = input("Enter a node and it's heuristic value seperated by spaces: ").split()
        neighbours = input(f"Enter the neighbours of {pair[0]} seperated by spaces: ").split()
        graph[pair[0]] = [neighbours,int(pair[1])]
        
    return graph


if __name__ == "__main__":
    graph = input_graph()
    dfs(graph)
    print()