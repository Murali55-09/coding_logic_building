# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List
class Solution:
    def hasDuplicates(self,nums: List[int] )-> bool:
        seen = set()        #hashset creation
        for num in nums:
            if num in seen:
                return True     #if element is already present then returns true
            else:
                seen.add(num)     #adding elements to the hashset
        return False

nums = [3, 4, 1, 5, 2]
res = Solution()
print(res.hasDuplicates(nums))

"""Learnings:
from typing import -- List	Enables type hint for list
List[int]-- Means list containing integers
-> bool	Means function returns a boolean value
A type hint in Python tells you (and your tools) what type of data a variable, parameter, or return value should have."""
        
