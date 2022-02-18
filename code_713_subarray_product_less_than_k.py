import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pointer_left = 0 # need to use sliding scale
        pointer_right = 0
        result = 0
        product = 1
        # if the value at i is less than k it's in
        for pointer_right in range(n):
            product *= nums[pointer_right]
            
            while product >= k and pointer_left <= pointer_right:
                product /= nums[pointer_left]
                pointer_left += 1
            result += pointer_right - pointer_left + 1
        return result