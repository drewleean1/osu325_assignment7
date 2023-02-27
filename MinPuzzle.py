#Name: Andrew Lee
#Assignment 7
#OSU CS 325
#Due Date: February 27, 2023

import heapq

def minEffort_helper(puzzle, coords):
    '''helper function that calculates the effort of a given path. returns inf if the given list is empty'''
    if coords == []:
        return float('inf')
    max_effort = 0
    heights = []
    for x in coords:                                            #did it this way for ease of comprehension
        m = x[0]
        n = x[1]
        heights.append(puzzle[m][n])
    for y in range(len(heights)-1):                             #go through heights to find effort of the path
        temp_effort = abs(heights[y] - heights[y+1])
        if temp_effort > max_effort:
            max_effort = temp_effort
    return max_effort

def minEffort(puzzle):
    '''function takes a 2D (mxn) array and finds the mininmum effort to get from (0,0) to the most bottom right cell or
    (m-1,n-1). The function is inspired by Djikstra algorithm code in the exploration. Instead of using a dictionary to
    keep track of shortest distances, we are going to use the dictionary (named effort in this function) to store the
    path to get that coordinate in dictionary, including that coordinate. We will use a helper function to calculate
    the effort of every path. When we finish processing everything, effort[m-1][n-1] will have the path with the
    minEffort which we can then use our help function.'''
    target_m = len(puzzle)-1
    target_n = len(puzzle[0])-1
    effort = {}                                                 #dictionary to store paths to each coord
    for x in range(target_m+1):                                 #adding every coord to the dict
        for y in range(target_n+1):
            effort[x,y] = []
    effort[0,0] = [(0,0)]                                       #necessary to build paths in later code
    pq = [(0,0)]                                                #our queue to do BFS.
    visited = []                                                #keep track of coords we visited
    while len (pq) > 0:
        current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.append(current_node)
        m = current_node[0]
        n = current_node[1]
        for neighbor in [(m-1, n), (m+1, n), (m, n+1), (m, n-1)]:       #check every neighbor
            if neighbor not in effort:
                continue
            if neighbor in visited:
                continue
            path = effort[current_node].copy()                          #copy of the current node's path
            path.append(neighbor)                                       #add neighbor to the path
            current_effort = minEffort_helper(puzzle, path)             #calculate effort of this path
            if current_effort < minEffort_helper(puzzle, effort[neighbor]):
                #if current_effort < effort of neighbor's path, then we found a new min effort path to get to neighbor
                effort[neighbor] = path
            heapq.heappush(pq, (neighbor))
    return minEffort_helper(puzzle, effort[target_m, target_n])

