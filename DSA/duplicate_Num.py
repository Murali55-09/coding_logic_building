# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List
class Solution:
    def hasDuplicates(self,nums: List[int] )-> bool:
        seen = set()
        for num in nums:
            if num in nums:
                return True
            else:
                seen.add(n)
        return False

nums = [3, 4, 1, 5, 2, 2, 3]
res = Solution()
print(res.hasDuplicates(nums))

"""Learnings:
from typing , import List	Enables type hint for list
List[int], Means list containing integers
-> bool	Means function returns a boolean value
A type hint in Python tells you (and your tools) what type of data a variable, parameter, or return value should have."""
        
