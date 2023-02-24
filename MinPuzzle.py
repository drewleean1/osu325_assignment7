

def minEffort_helper(puzzle, n, m, visited):
    current = puzzle[n][m]
    min = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    min_coords = (0,0)
    for x in [(n-1, m), (n+1, m), (n, m+1), (n, m-1)]:
        if (x[0], x[1]) in visited:
            continue
        elif x[0] < 0 or x[1] < 0 or x[0] > (len(puzzle[0])-1) or x[1]>(len(puzzle)-1):
            continue
        temporary = abs(current - puzzle[x[0]][x[1]])
        if temporary <= min:
            min = temporary
            min_coords = (x[0], x[1])
    if min_coords not in visited:
        visited.append(min_coords)
    return (min_coords, min)

def minEffort(puzzle):
    target_n = len(puzzle[0])-1
    target_m = len(puzzle)-1
    n = 0
    m = 0
    result = 0
    visited = [(0,0)]
    while m != target_m or n != target_n:
        lowest_effort = minEffort_helper(puzzle, n, m, visited)
        if lowest_effort[1] > result:
            result = lowest_effort[1]
        n = lowest_effort[0][0]
        m = lowest_effort[0][1]
    return result

print(minEffort([[1, 3, 5], [3, 8, 3], [3, 4, 5]]))

#print(minEffort_helper([[1, 3, 5], [3, 8, 3], [3, 4, 5]], 0, 2, [(0,0), (0,1), (0,2)]))