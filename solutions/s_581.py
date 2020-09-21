from typing import List

class Solution:
    """
    error
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 2
            return 0
        if nums[0] > nums[-1]:
            return len(nums)
        min_p, max_p = None, None
        flag = False
        for i in range(1, len(nums)-1):
            if (nums[i] - nums[i-1]) * (nums[i+1] - nums[i]) < 0:
                flag = True
                min_p = min(nums[i], min_p if min_p else nums[i])
                max_p = max(nums[i], max_p if max_p else nums[i])
        if not flag:
            return 0
        for l in range(len(nums)):
            if nums[l] > min_p:
                break
            l += 1
        r = len(nums) - 1
        while r >= 0:
            if nums[r] < max_p:
                break
            r -= 1
        print(l, r, min_p, max_p)
        return r - l + 1

if __name__ == "__main__":
    s = Solution()
    l = [1,3,2,4,5]
    #l = [1,3,2,2,2]
    l = [1,3,2]
    print(s.findUnsortedSubarray(l))
    pass
