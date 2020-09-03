class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        i = 0
        while i < len(nums):
            a = nums[i]
            b = target - a
            if b != a and b in num_map:
                return [num_map[b], i]
            num_map[a] = i
            i += 1
        return []
