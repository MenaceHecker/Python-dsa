## Rotting Oranges
## You are given an m x n grid where each cell can have one of three values:
## 0 representing an empty cell,
## 1 representing a fresh orange, or
## 2 representing a rotten orange.
## Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
## Return the minimum number of minutes that must elapse until no cell has a fresh orange
## If this is impossible, return -1.

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1) 
            ]
        minutes = 0 
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if ( 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
                
            minutes += 1
        if fresh > 0:
            return -1
        return minutes

                    

        