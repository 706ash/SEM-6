class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, node):
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.f)
    
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def contains_better_path(self, name, f_score):
        return any(node.name == name and node.f <= f_score for node in self.queue)

def a_star_algorithm(start, goal, graph, heuristic):
    open_list = PriorityQueue()
    closed_list = set()

    start_node = Node(start, None, 0, heuristic[start])
    open_list.push(start_node)

    while not open_list.is_empty():
        current_node = open_list.pop()

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g, h)

            if open_list.contains_better_path(neighbor, neighbor_node.f):
                continue

            open_list.push(neighbor_node)

    return None  # No path found

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'D': 1, 'E': 5},
        'C': {'A': 3, 'F': 2},
        'D': {'B': 1},
        'E': {'B': 5, 'F': 2},
        'F': {'C': 2, 'E': 2}
    }

    heuristic = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 2,
        'E': 6,
        'F': 0
    }

    start = 'A'
    goal = 'F'
    path = a_star_algorithm(start, goal, graph, heuristic)
    print("Path:", path)