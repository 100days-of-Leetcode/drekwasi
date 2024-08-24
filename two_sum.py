"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_nums = len(nums)
        if length_nums == 2:
            return [0, 1]

        for i in range(length_nums):
            for j in range(i + 1, length_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

# One pass solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length_nums = len(nums)
        if length_nums == 2:
            return [0, 1]
        prevMap = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [index, prevMap[diff]]
            prevMap[num] = index