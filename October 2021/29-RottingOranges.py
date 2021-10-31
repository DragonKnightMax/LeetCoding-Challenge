class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 0-empty
        # 1-fresh
        # 2-rotten
        
        # No solution
        if len(grid) == 0:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        
        # Keep track of rotten oranges coordinates
        rotten_locs = deque()
        
        # Number of fresh oranges left
        fresh_num = 0
        
        # Find fresh and rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_num += 1
                elif grid[i][j] == 2:
                    rotten_locs.append((i, j))
        
        # Record minutes passed
        timer = 0
        
        # 4-directionally adjacent cells (top, right, bottom, left)
        adjacents = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Rotting happens
        while fresh_num > 0 and rotten_locs:
            # Get a rotten orange loc from deque
            x, y = rotten_locs.popleft()
            
            # Visit every adjacent cells
            for dx, dy in adjacents:
                x2, y2 = x+dx, y+dy
                
                # Ensure x2 and y2 are within range
                if x2 < 0 or x2 >= rows or y2 < 0 or y2 >= cols:
                    continue
                
                # Fresh orange becomes rotten
                if grid[x2][y2] == 1:
                    grid[x2][y2] == 2
                    fresh_num -= 1
                    
                    # Add new rotten orange coordinates
                    rotten_locs.append((x2, y2))
                
            # Increment timer after rotting
            timer += 1
                    
        return timer if fresh_num == 0 else -1
