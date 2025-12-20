from typing import List  ## for taking interger type input of the list

class Solution:
    def duplicate(self, nums: List[int]) -> bool:       ## returns boolean
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False
    
list1 = [1, 2, 3, 5, 7]
sol = Solution()
print(sol.duplicate(list1))  
