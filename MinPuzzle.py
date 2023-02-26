
import heapq

def minEffort_helper(puzzle, n, m, visited, result):
    current = puzzle[n][m]
    #min = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    min_coords = (0,0)
    if current not in visited:
        #print(current)
        visited.append(current)
        #print(visited)
        for x in [(n-1, m), (n+1, m), (n, m+1), (n, m-1)]:
            if (x[0], x[1]) in visited:
                continue
            elif x[0] < 0 or x[1] < 0 or x[0] > (len(puzzle[0])-1) or x[1]>(len(puzzle)-1):
                continue
            temporary = abs(current - puzzle[x[0]][x[1]])
            if temporary >= result:
                result = temporary
                minEffort_helper(puzzle, x[0], x[1], visited, result)

    #if min_coords not in visited:
    #    visited.append(min_coords)
    #return (min_coords, min)

def minEffort2(puzzle):
    target_n = len(puzzle[0])-1
    target_m = len(puzzle)-1
    #n = 0
    #m = 0
    result = 0
    visited = [(0,0)]
    for n in range (len(puzzle[0])):
        for m in range(len(puzzle)):
            #print((n,m))
            minEffort_helper(puzzle, n, m, visited, result)
    '''while m != target_m or n != target_n:
        lowest_effort = minEffort_helper(puzzle, n, m, visited)
        if lowest_effort[1] > result:
            result = lowest_effort[1]
        n = lowest_effort[0][0]
        m = lowest_effort[0][1]'''
    return result

#print(minEffort_helper([[1, 3, 5], [3, 8, 3], [3, 4, 5]], 0, 2, [(0,0), (0,1), (0,2)]))


def minEffort(puzzle):
    print(puzzle)
    target_n = len(puzzle[0])-1
    target_m = len(puzzle)-1
    effort = {}
    for x in range(target_m+1):
        for y in range(target_n+1):
            effort[x,y] = float('inf')
    effort[(0,0)] = 0
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
            if current_effort < effort[x]:
                effort[x] = current_effort
                heapq.heappush(pq, (x))

    print(effort[(target_m, target_n)])
    return effort[(target_m, target_n)]

print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))

