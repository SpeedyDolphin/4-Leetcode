
class RecursiveSolution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        self.obstacleGrid = obstacleGrid
        return self.numPaths(0,0)

    def numPaths(self, row, col)->int:
        if(row >= len(self.obstacleGrid) or col >= len(self.obstacleGrid[0])): #out of bounds checking
           return 0
        if(self.obstacleGrid[row][col] == 1): #obstacle checking
            return 0
        if(row == len(self.obstacleGrid) -1 and col == len(self.obstacleGrid[0])-1): #out of bounds checking
            return 1
        
        return self.numPaths(row, col+1) + self.numPaths(row+1, col)

class ItterativeSolution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        dpGrid = []
        for i in range(len(obstacleGrid)):
            dpGrid.append([])
            for j in range(len(obstacleGrid[0])):
                dpGrid[i].append(0)

        for col in range(len(obstacleGrid[0])): 
            if(obstacleGrid[0][col] == 1): #obstacle checking
                break
            dpGrid[0][col] = 1

        for row in range(len(obstacleGrid)): 
            if(obstacleGrid[row][0] == 1): #obstacle checking
                break
            dpGrid[row][0] = 1

        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if(obstacleGrid[row][col] == 1): #obstacle checking
                    dpGrid[row][col] = 0 
                else:
                    dpGrid[row][col] = dpGrid[row-1][col] + dpGrid[row][col-1]

        return dpGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] 







#TESTCASE
test = ItterativeSolution()
print(test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))