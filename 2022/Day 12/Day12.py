from string import ascii_lowercase
from heapq import heappop, heappush


with open("Day12.txt") as file:
    lines = file.read().strip().split()

#print(lines)

grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])
#print(grid)

for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        if letter == "S":
            start = i, j
        if letter == "E":
            end = i, j

#print(start, end)

def height(z):
    if z in ascii_lowercase:
        return ascii_lowercase.index(z)
    if z == "S":
        return 0
    if z == "E":
        return 25


#=== use Dijkstra's algorithm (decision theory) ===

# Determine valid neighbours
def neighbors(i,j):
    for di, dj in [[1,0], [-1,0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j +dj

        # Check we are still in the matrix
        if not (0 <= ii < n and 0 <= jj < m):
            continue

        #retun what fits criteria
        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii, jj


# Dijkstra's

# grid of n*m all of flase that we turn to true as we visit
visited = [[False] * m for _ in range(n)]
#print(visited)

#heap or priority queue to find shortest, shortest steps to start (0)
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    #skip if visited
    if visited[i][j]:
        continue

    # make sure we don't come back 
    visited[i][j] = True 

    if (i, j) == end:
        print(steps)
        break

    for ii, jj in neighbors(i, j):
        heappush(heap, (steps + 1, ii, jj))


# == Step 2 ==

# start at the end and head back, start E and end at any a

#can only move backwards now
def neighbors(i,j):
    for di, dj in [[1,0], [-1,0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j +dj

        # Check we are still in the matrix
        if not (0 <= ii < n and 0 <= jj < m):
            continue

        #retun what fits criteria
        if height(grid[ii][jj]) >= height(grid[i][j]) + -1:
            yield ii, jj


# Dijkstra's

# grid of n*m all of flase that we turn to true as we visit
visited = [[False] * m for _ in range(n)]
#print(visited)

#heap or priority queue to find shortest, shortest steps to start (0)
heap = [(0, end[0], end[1])]

while True:
    steps, i, j = heappop(heap)

    #skip if visited
    if visited[i][j]:
        continue

    # make sure we don't come back 
    visited[i][j] = True 

    if height(grid[i][j]) == 0:
        print(steps)
        break

    for ii, jj in neighbors(i, j):
        heappush(heap, (steps + 1, ii, jj))