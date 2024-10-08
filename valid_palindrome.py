"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for i in s:
            if i.isalnum():
                clean_s += i.lower()

        return clean_s == clean_s[::-1]

# Two pointer solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1
        
        return True

    def isAlphaNum(self, c):
        if(( ord('A') <= ord(c) <= ord('Z')) or 
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
        ):
            return True
        