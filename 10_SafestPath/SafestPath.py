'''
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.
'''
from collections import namedtuple, deque
import heapq

X = namedtuple('X', ['col', 'row', 'val'])
Y = namedtuple('Y', ['spotSafe', 'voyageSafe'])

def maximumSafenessFactor(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    maxCol = len(grid)
    maxRow = len(grid[0])
    if grid[0][0] == 0 or grid[maxCol][maxRow] == 0:
        return 0 
    
    disGrid = distanceGrid(grid)
    disGrid[0][0].voyageSafe = disGrid[0][0].spotSafe
    heap = heapq()

    

def distanceGrid(grid):
    disGrid = [[0] * len(grid[0]) for i in range(len(grid))]
    toVisit : deque = deque()
    visited : set = set()

    #find all of the thieves
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[col][row] == 1:
                visited.add((col, row))
                
                potential = [(col+1, row+1), (col-1, row-1), (col+1,row-1), (col-1, row+1)]
                for cell in potential: 
                    if cell[0] >= 0 and cell[1] >= 0 and cell[0] < len(grid) and cell[1] < len(grid[0]):
                        toVisit.append(X(cell[0], cell[0], 1))

    while len(toVisit) > 0: 
        visiting = toVisit.popleft()
        if visiting in visited:
            pass
        
        disGrid[visiting.col][visiting.row] = Y(visiting.val, -1)
        visited.add

        potential = [(col+1, row+1), (col-1, row-1), (col+1,row-1), (col-1, row+1)]
        for cell in potential: 
            if cell[0] >= 0 and cell[1] >= 0 and cell[0] < len(grid) and cell[1] < len(grid[0]): # check bounds
                toVisit.append(X(cell[0], cell[0], visiting.val+1))

    return disGrid


