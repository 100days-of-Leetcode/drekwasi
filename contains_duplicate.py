"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = []

        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.append(num)
        return False
