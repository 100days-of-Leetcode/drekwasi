"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for n in nums_set:
            left = n - 1
            count = 0
            if left not in nums_set:
                count += 1
                while n + 1 in nums_set:
                    count += 1
                    n += 1
                if count > max_count:
                    max_count = count

        return max_count