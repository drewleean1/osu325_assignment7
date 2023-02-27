
import heapq

def minEffort(puzzle):
    target_n = len(puzzle[0])-1
    target_m = len(puzzle)-1
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
            # Only consider this new path if it's better than any path we've
            # already found.
            if current_effort < effort[x][0]:
                effort[x] = (current_effort, (m,n))
                heapq.heappush(pq, (x))
    max_effort = 0
    end_of_list = (target_m, target_n)
    while end_of_list != (0,0):
        if effort[end_of_list][0] > max_effort:
            max_effort = effort[end_of_list][0]
        end_of_list = effort[end_of_list][1]
    return max_effort


