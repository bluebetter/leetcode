from typing import List
import sys

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_p, max_p = sys.maxsize, -sys.maxsize - 1
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                min_p = min(min_p, nums[i])
                flag = False
        flag = False
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                flag = True
            if flag:
                max_p = max(max_p, nums[i])
                flag = False
            i -= 1
        
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if nums[l] > min_p:
                break
            l += 1
        while r >= 0:
            if nums[r] < max_p:
                break
            r -= 1

        return r - l + 1 if r > l else 0

if __name__ == "__main__":
    s = Solution()
    #l = [1,3,2,4,5]
    #l = [1,3,2,2,2]
    l = [1,2,3,3,3]
    l = [1,3,2]
    print(s.findUnsortedSubarray(l))
    pass
