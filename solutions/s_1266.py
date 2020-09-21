from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x0, y0 = points[0]
        ans = 0
        for i in range(1, len(points)):
            x1, y1 = points[i]
            ans += max(abs(x1 - x0), abs(y1 - y0))
            x0, y0 = x1, y1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
    pass
