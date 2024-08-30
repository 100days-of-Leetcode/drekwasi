"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# Slow solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        water_vol = []
        for i in range(0, len(height)):
            for j in range(0, len(height)):
                if j == i:
                    continue
                min_height = min(height[i], height[j])
                distance = j - i
                water_vol.append(min_height * distance)
        
        return max(water_vol)


# Two pointer solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            elif height[r] > height[l]:
                l += 1
            else:
                l += 1
        
        return max_area