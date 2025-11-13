# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
from typing import List
class Solution:
    def twoSum(self, a: List[int], target: int ) -> List[int]:          #return type List
        # logic
        prevMap = {}        # Hashmap creation (Dict)
        for  i, n in enumerate(a):      #usiing enum for index retrival   
            diff = target - n           
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return



a = [2, 3, 5, 2, 3, 4]
target = 5
res = Solution()
result = res.twoSum(a, target)
print(result)
