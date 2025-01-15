def movegen(current, graph):
    node_list = []
    neighbours = graph[current]
    for n in neighbours:
        temp = [n, current]
        node_list.append(temp)

    return node_list


def goal_test(current, goal):
    if current == goal:
        return True


def bfs(graph):
    open = []
    closed = []
    
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    
    open.append([start_node,None])
    # print(open)
    
    while True:
        current = open[0][0]
        if goal_test(current, goal_node) or open == []:
            print("\n\nGoal found\n", closed)
            break                    
        else:
            child_list = movegen(current, graph)
            for child in child_list:
                for o in open:
                    if child[0] == o[0]:
                        break
                else:
                    for c in closed:
                        if child[0] == c[0]:
                            break
                    else:
                        open.append(child)
            closed.append(open[0])
            del open[0]
            
            
def input_graph():
    graph = {}

    n = int(input("Enter the number of nodes: "))
    
    for i in range(n):
        node = input("Enter a node: ")
        neighbours = input(f"Enter the neighbours of {node} seperated by spaces: ").split()
        graph[node] = neighbours

    print(graph)
    return graph

if __name__ == "__main__":
    graph = input_graph()
    bfs(graph)