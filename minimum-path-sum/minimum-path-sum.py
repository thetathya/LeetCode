class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if i==len(grid)-1 and j!=len(grid[0])-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                elif i!=len(grid)-1 and j!=len(grid[0])-1:
                    grid[i][j] = grid[i][j] + min(grid[i][j+1],grid[i+1][j])
                elif j==len(grid[0])-1 and i!=len(grid)-1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]
        return grid[0][0]