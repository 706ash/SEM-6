def movegen(current, graph):
    return [[n, current, graph[n][1]] for n in graph[current][0]]

def traversal(closed):
    path = '  -->  '.join(c[0] for c in closed)
    print(f"Traversal: {path}")

def goal_test(current, goal_nodes):
    return current in goal_nodes

def goal_list_fn(graph, mode):
    if mode == 1:
        best_h = min(v[1] for v in graph.values())
    else:
        best_h = max(v[1] for v in graph.values())
    return [k for k, v in graph.items() if v[1] == best_h]

def steepest_ascent_hill_climbing(graph, mode):
    open_list, closed = [], []
    start_node = input("Enter the start node: ")
    goal_nodes = goal_list_fn(graph, mode)
    global_optimum_h = graph[goal_nodes[0]][1]

    if start_node not in graph:
        print("Start node is not present in the entered graph")
        return

    open_list.append([start_node, None, graph[start_node][1]])

    while open_list:
        current = open_list.pop(0)
        closed.append(current)

        if goal_test(current[0], goal_nodes):
            print("\n✅ Goal Found!")
            traversal(closed)
            if current[2] == global_optimum_h:
                print("🔵 Global Optimum Reached")
            else:
                print("🟡 Local Optimum Reached (Not Global)")
            return

        neighbours = movegen(current[0], graph)
        if not neighbours:
            print("\n⚠️ No more neighbors to explore.")
            break
        
        fn = min if mode == 1 else max
        best = fn(neighbours, key=lambda x: x[2])

        # Plateau detection (no improvement)
        if best[2] == current[2]:
            print("\n⚠️ Plateau Detected: No improvement in heuristic.")
            break

        # Overestimation / Underestimation Reporting
        if (mode == 1 and best[2] > global_optimum_h):
            print("🔺 Heuristic Overestimation: Best neighbor is farther from optimal.")
        elif (mode == 1 and best[2] < global_optimum_h):
            print("🔻 Heuristic Underestimation: Moving closer to optimal.")
        elif (mode == 2 and best[2] < global_optimum_h):
            print("🔺 Heuristic Underestimation: Best neighbor is below expected global.")
        elif (mode == 2 and best[2] > global_optimum_h):
            print("🔻 Heuristic Overestimation: Best neighbor is above global.")

        # Check if no better neighbor exists
        if (mode == 1 and best[2] >= current[2]) or (mode == 2 and best[2] <= current[2]):
            print("\n🟥 Local Optimum Reached (No better neighbor)")
            break

        open_list.append(best)

    traversal(closed)
    print("🟡 Final Heuristic at Stop:", current[2])
    print("🔵 Global Optimum Heuristic:", global_optimum_h)


def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node, h = input("Enter the node and its heuristic (space separated): ").split()
        neighbours = input(f"Enter the neighbours of {node} (space separated): ").split()
        graph[node] = [neighbours, int(h)]
    return graph

if __name__ == "__main__":
    graph = input_graph()
    mode = int(input("Enter 1 for minimization and 2 for maximization: "))
    steepest_ascent_hill_climbing(graph, mode)
