class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        track_s = {}
        track_t = {}

        for char in s:
            if char not in t:
                return False
            track_s[char] = 1
            if track_s.get(char):
                track_s[char] += 1

        for char in t:
            track_t[char] = 1
            if track_t.get(char):
                track_t[char] += 1

        for key in track_s.keys():
            if track_s[key] != track_t.get(key):
                return False

        return True
