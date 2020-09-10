class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t_map = {}
        for n in nums:
            if n not in t_map:
                t_map[n] = 0
            t_map[n] += 1
            if t_map[n] >= len(nums) / 2:
                return n
        return -1
