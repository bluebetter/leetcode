from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2, idx = -1, -1, -1
        for i, val in enumerate(nums):
            if val > max1:
                idx = i
                max2 = max1
                max1 = val
            elif val > max2:
                max2 = val
        print(max1, max2, idx)
        return idx if max1 >= max2 * 2 else -1

if __name__ == "__main__":
    s = Solution()
    #s.dominantIndex([0, 0, 0, 1])
    s.dominantIndex([1,2,16,35,44,100,27,0])
    pass