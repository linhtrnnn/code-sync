class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]#for search

        isl = 0 #num of islands

        def search(i, j):
            if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid):
                return
            if visited[i][j] == 1 or grid[i][j] == "0":
                return 
            else:
                visited[i][j] = 1
                for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
                    search(i+di, j+dj)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    isl += 1
                    search(i, j)

        return isl