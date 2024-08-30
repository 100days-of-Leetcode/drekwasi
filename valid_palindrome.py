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