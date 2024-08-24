"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        track_s = {}
        track_t = {}

        for i in range(len(s)):
            if s[i] not in t:
                return False

            track_s[s[i]] = 1 + track_s.get(s[i], 0)
            track_t[t[i]] = 1 + track_t.get(t[i], 0)

        for key in track_s.keys():
            if track_s[key] != track_t.get(key):
                return False

        return True


# Memory O(1) solution
# Some interviewers view sorting as O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
