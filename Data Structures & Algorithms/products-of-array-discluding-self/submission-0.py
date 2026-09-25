class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        left = 1
        zero_count = 0

        for num in nums:
            if num:
                left *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return output

        for i, num in enumerate(nums):
            if zero_count:
                if num != 0:
                    output[i] = 0
                else:
                    output[i] = left
            else:
                output[i] = left // num
        return output

             