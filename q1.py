test =  [['A','B',3], ['A', 'E', 3], ['E', 'F', 1], ['F', 'G', 1], ['G', 'D', 1], ['C', 'D', 1], ['B', 'C', 2]]
from collections import defaultdict

def build_graph(test):
    # point to connections map
    graph = defaultdict(list)
    # route to distance map
    times = {}
    # construct graphs
    for a, b, time in test:
        graph[a].append(b)
        times[(a, b)] = time
    return graph, times

def dfs(graph, startNode, visited, finalNode, stops, times, final_time):
    # base
    if startNode == finalNode and stops <= 3 and final_time < 6:
        return True
    if startNode in visited or final_time > 5:
        return False
    visited.add(startNode)
    ans = False
    for node in graph[startNode]:
        if dfs(graph, node, visited, finalNode, stops + 1, times, times[(startNode, node)] + final_time ):
            return True
    return False

def main_func(test, a, b):
    graph, times = build_graph(test)
    ans = dfs(graph, a, set(), b, -1, times, 0)
    print(ans)

# main_func(test)
tests = [['A', 'C'], ['A', 'D'], ['A', 'G']]

for a, b in tests:
  main_func(test, a, b)