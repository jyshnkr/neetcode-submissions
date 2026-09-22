class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = sorted(set(nums))
        nums[:len(unique_set)] = unique_set
        return len(unique_set)