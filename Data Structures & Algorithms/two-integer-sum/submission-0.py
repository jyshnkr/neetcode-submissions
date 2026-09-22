class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in indices_map:
                return [indices_map[diff], idx]
            indices_map[num] = idx