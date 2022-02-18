import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pointer_right = 0
        result = 0
        r2 = list()
        # if the value at i is less than k it's in
        for i in range(n):
            pointer_right = min(i + 1, n-1)
            if nums[i] < k:
                result += 1
                r2.append(nums[i])
            if i == pointer_right:
                continue
            while math.prod(nums[i:pointer_right+1]) < k and pointer_right < n:
                r2.append(nums[i:pointer_right+1])
                result += 1
                pointer_right += 1

        return result