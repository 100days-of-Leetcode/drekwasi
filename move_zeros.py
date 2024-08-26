"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        nums_length = len(nums)
        arr = []
        for index, n in enumerate(nums):
            if n == 0 and index != nums_length - 1 :
                arr.append(n)

        for zero in arr:
            nums.remove(zero)
            nums.extend(arr)

