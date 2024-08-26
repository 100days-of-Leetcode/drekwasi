"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people) - 1
        left = 0
        boat_number = 0

        while right >= left:
            if right == left:
                boat_number += 1
                break
            if people[left] + people[right] > limit:
                boat_number += 1
                right -= 1
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
                boat_number += 1

        return boat_number
