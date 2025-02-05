open = [['A', None, 0],['B', 'A', 2],['C', 'B', -1]]
min = open[0]
for i in range(1, len(open)):
    if open[i][2] < min[2]:
        min = open[i]
print(min[0])

# graph = {
#     'A': [['B', 'C'], 6],
#     'B': [['D', 'E'], 4],
#     'C': [['F', 'G'], 5],
#     'D': [[], 3],
#     'E': [['H'], 2],
#     'F': [[], 3],
#     'G': [[], 4],
#     'H': [[], 1]  # Goal Node
#     }
# current = 'A'
# print([[n, current, graph[n][1]] for n in graph[current][0]])