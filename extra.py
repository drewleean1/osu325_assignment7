


import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}

def minEffort(puzzle):
    print(puzzle)
    target_n = len(puzzle[0]) - 1
    target_m = len(puzzle) - 1
    effort = {}
    for x in range(target_m + 1):
        for y in range(target_n + 1):
            effort[x, y] = float('inf')
    effort[(0, 0)] = 0
    pq = [(0, 0)]
    visited = []
    print(effort)
    while len(pq) > 0:
        current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.append(current_node)
        m = current_node[0]
        n = current_node[1]
        for x in [(m - 1, n), (m + 1, n), (m, n + 1), (m, n - 1)]:
            if x not in effort:
                continue
            if x in visited:
                continue
            current_effort = abs(puzzle[m][n] - puzzle[x[0]][x[1]])
            # Only consider this new path if it's better than any path we've
            # already found.
            if current_effort < effort[x]:
                effort[x] = current_effort
                heapq.heappush(pq, (x))

    print(effort[(target_m, target_n)])
    return effort[(target_m, target_n)]
print(minEffort([[1, 2, 2, 3], [3, 8, 2, 5], [5, 3, 6, 8]]))

'''
Reference:
source: https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
'''

def minEffort(puzzle):
    print(puzzle)
    target_m = len(puzzle)-1
    target_n = len(puzzle[0])-1
    effort = {}
    for x in range(target_m+1):
        for y in range(target_n+1):
            effort[x,y] = (float('inf'), (0,0))
    effort[(0,0)] = (0, (0,0))
    pq = [(0,0)]
    visited = []
    while len (pq) > 0:
        current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.append(current_node)
        m = current_node[0]
        n = current_node[1]
        for x in [(m-1, n), (m+1, n), (m, n+1), (m, n-1)]:
            if x not in effort:
                continue
            if x in visited:
                continue
            current_effort =  abs(puzzle[m][n] - puzzle[x[0]][x[1]])
            if current_effort < effort[x][0]:
                effort[x] = (current_effort, (m,n))
                heapq.heappush(pq, (x))
    max_effort = 0
    end_of_list = (target_m, target_n)
    for x in effort:
        print(x, effort[x])
    while end_of_list != (0,0):
        if effort[end_of_list][0] > max_effort:
            max_effort = effort[end_of_list][0]
        end_of_list = effort[end_of_list][1]
    return max_effort