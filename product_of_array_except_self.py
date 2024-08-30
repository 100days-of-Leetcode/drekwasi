"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Slow solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j :
                    answer[i] = answer[i] * nums[j]

        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)

        prefix = 1
        results = [1] * length_nums

        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]

        return results

