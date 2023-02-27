
import heapq
"""
def minEffort(puzzle):
    print(puzzle)
    target_m = len(puzzle)-1
    target_n = len(puzzle[0])-1
    effort = {}
    for x in range(target_m+1):
        for y in range(target_n+1):
            effort[x,y] = (float('inf'), (0,0))
    #effort[(0,0)] = (float('inf'), (0,0))
    pq = [(0,0)]
    visited = []
    while len (pq) > 0:
        current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.append(current_node)
        m = current_node[0]
        n = current_node[1]
        for neighbor in [(m-1, n), (m+1, n), (m, n+1), (m, n-1)]:
            if neighbor not in effort:
                continue
            if neighbor in visited:
                continue
            current_effort =  abs(puzzle[m][n] - puzzle[neighbor[0]][neighbor[1]])
            print(current_node, neighbor, puzzle[neighbor[0]][neighbor[1]], current_effort)

            if current_effort < effort[neighbor][0]:
                effort[neighbor] = (current_effort, neighbor)
                if current_effort <= effort[(m,n)][0]:
                    effort[(m,n)] = (effort[(m,n)][0], neighbor)
                heapq.heappush(pq, (neighbor))
    effort[(0,0)] = (0, effort[(0,0)][1])
    max_effort = 0
    end_of_list = (0, 0)
    print('---------------')
    for x in effort:
        print(x, effort[x])
    while end_of_list != (target_m, target_n):
        if effort[end_of_list][0] > max_effort:
            max_effort = effort[end_of_list][0]
        end_of_list = effort[end_of_list][1]
    if effort[end_of_list][0] > max_effort:
        max_effort = effort[end_of_list][0]
    return max_effort
"""

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

    return effort[(target_m, target_n)]

