from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        len_r, len_c = len(grid), len(grid[0])
        new_grid = [[0]*len_c for _ in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                new_r = (r + (k + c) // len_c) % len_r
                new_c = (c + k) % len_c
                new_grid[new_r][new_c] = grid[r][c]
        return new_grid

if __name__ == "__main__":
    grid = [[1,2,3], [4,5,6], [7,8,9]]
    s = Solution()
    print(s.shiftGrid(grid, 9))
    pass