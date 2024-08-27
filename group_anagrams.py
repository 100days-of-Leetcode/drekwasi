"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
import defaultdict from collections
# n log n + n**2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        sorted_strs = ["".join(sorted(x)) for x in strs]

        output = []
        used_indices = set()
        for i, s in enumerate(sorted_strs):
            if s[1] in used_indices:
                continue
            comparison = [strs[s[1]]]
            used_indices.add(s[1])

            for j in range(i + 1, len(sorted_strs)):
                if s[0] == sorted_strs[j][0]:
                    comparison.append(strs[sorted_strs[j][1]])
                    used_indices.add(sorted_strs[j][1])
            output.append(comparison)

        return output

# m* n
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()
