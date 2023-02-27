
import heapq

def minEffort_helper(puzzle, coords):
    if coords == []:
        return float('inf')
    max_effort = 0
    heights = []
    for x in coords:
        m = x[0]
        n = x[1]
        heights.append(puzzle[m][n])
    for y in range(len(heights)-1):
        temp_effort = abs(heights[y] - heights[y+1])
        if temp_effort > max_effort:
            max_effort = temp_effort
    return max_effort

def minEffort(puzzle):
    print(puzzle)
    target_m = len(puzzle)-1
    target_n = len(puzzle[0])-1
    effort = {}
    for x in range(target_m+1):
        for y in range(target_n+1):
            #effort[x,y] = (float('inf'), (0,0))
            effort[x,y] = []
    #effort[(0,0)] = (float('inf'), (0,0))
    effort[0,0] = [(0,0)]
    #print(effort)
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
            current_list = []
            for x in effort[current_node]:                          #prevent issues with global var
                current_list.append(x)
            current_list.append(neighbor)
            #print(current_list)
            current_effort = minEffort_helper(puzzle, current_list)
            #print(current_effort)
            if current_effort < minEffort_helper(puzzle, effort[neighbor]):
                effort[neighbor] = current_list
            heapq.heappush(pq, (neighbor))
    return minEffort_helper(puzzle, effort[target_m, target_n])
    """ current_effort  =  abs(puzzle[m][n] - puzzle[neighbor[0]][neighbor[1]])
            print(current_node, neighbor, puzzle[neighbor[0]][neighbor[1]], current_effort)

            if current_effort < effort[neighbor][0]:
                effort[neighbor] = (current_effort, neighbor)
                if current_effort <= effort[(m,n)][0]:
                    effort[(m,n)] = (effort[(m,n)][0], neighbor)
                heapq.heappush(pq, (neighbor))"""
    """effort[(0,0)] = (0, effort[(0,0)][1])
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
    return max_effort"""

tests = [   [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 3, 5], [2, 8, 3], [3, 4, 5]],
            [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
            [[1, 2, 2, 3], [3, 8, 2, 5], [5, 3, 4, 8]],
            [[1, 3, 5], [3, 8, 7], [5, 3, 9], [7, 9, 6]]
]
#print (minEffort_helper([[1, 3, 5], [2, 8, 3], [3, 4, 5]], []))
#print(minEffort(tests[2]))
for x in tests:
    print(minEffort(x))