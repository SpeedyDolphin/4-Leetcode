#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

def updateMatrix(mat: 'list(list(int))') -> 'list(list(int))':
    queue : set = set()
    seen : set = set()
    solution : list = list()

    #setup
    for i in range(len(mat)):
        solution.append(list())
        for j in range(len(mat[0])):
            if(mat[i][j] == 0):
                solution[i].append(0)
                queue.add((i,j))
                seen.add((i,j))
            else:
                solution[i].append(-1)

    ct = 1
    while(len(queue) > 0):
        neighbors : set = set()
        for x, y in queue: 
            expansions = [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]
            for newCoord in expansions:
                if(newCoord in seen):
                    continue
                if newCoord[0] >= len(mat) or newCoord[0] < 0 or newCoord[1] >= len(mat[0]) or newCoord[1] < 0:
                    continue

                seen.add(newCoord)
                neighbors.add(newCoord)
                solution[newCoord[0]][newCoord[1]] = ct
        
        ct+=1
        queue = set(neighbors)
        neighbors.clear()
    
    return solution

print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))


