class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row, col = len(grid), len(grid[0])
        
        # Start at top left
        for i in range(row):
            for j in range(col):
                
                # Island (square)
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    # Check for neighbours (down and right)
                    if i < row-1 and grid[i+1][j] == 1:
                        perimeter -= 2
                    if j < col-1 and grid[i][j+1] == 1:
                        perimeter -= 2
        
        return perimeter         
