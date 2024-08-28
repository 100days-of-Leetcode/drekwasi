"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        return [sorted_counts[x][0] for x in range(0, k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for k, v in count.items():
            freq[v].append(k)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result