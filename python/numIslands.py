from typing import List


class Solution:
    IS_ISLAND = "1"
    IS_VISITED = "2"

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == Solution.IS_ISLAND:
                    grid[x][y] = Solution.IS_VISITED

                    self.dfs(grid, x, y)
                    # self.bfs(grid, x, y)

                    num_islands += 1

        return num_islands

    def dfs(self, grid, x, y):
        point_x, point_y = x, y

        for direction_x, direction_y in Solution.directions:
            x = point_x + direction_x
            y = point_y + direction_y

            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                if grid[x][y] == Solution.IS_ISLAND:
                    grid[x][y] = Solution.IS_VISITED

                    self.dfs(grid, x, y)

    def bfs(self, grid, x, y):
        queue = []
        queue.append((x, y))

        while queue:
            point_x, point_y = queue.pop()

            for direction_x, direction_y in Solution.directions:
                x = point_x + direction_x
                y = point_y + direction_y

                if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                    if grid[x][y] == Solution.IS_ISLAND:
                        grid[x][y] = Solution.IS_VISITED

                        queue.append((x, y))

