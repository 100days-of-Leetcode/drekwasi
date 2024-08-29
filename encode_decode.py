"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        enc = ""
        for s in strs:
            enc.join(f"{len(s)}#{s}")
        return enc

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            i = j
            while j != "#":
                j += 1
            num_chars = int(str[i:j])
            full_str = str[j + 1: j + 1 + num_chars]
            res.append(full_str)
            i = j + 1 + num_chars