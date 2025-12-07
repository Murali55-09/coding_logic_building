# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from typing import List
class Solution:
    def groupAnagram(self, names: List[str]) -> List[int]:
        # logic
        res = {}
        for s in names:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in res:    # manually check & create list
                res[key] = []

            res[key].append(s)    # add word to the list)
        return list(res.values())


    

names = ["mat", "hat", "tam", "amt", "cat"]
res = Solution()
result = res.groupAnagram(names)
print(result)