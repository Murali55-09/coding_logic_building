# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
""" conditions:
contains the exact same characters as another string
order of the characters can be different.
"""

class Solution:
    def anagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        
        countA = {}         #dictnory to save frequency of characters in string a
        countB = {}         #dictnory to save frequency of characters in string b

        for i in range(len(a)):
            countA[a[i]] = 1 + countA.get(a[i], 0)      #{'m':1,'r':1,'k':1}, if character is not found it put value as 0
            countB[b[i]] = 1 + countB.get(b[i], 0)      #{'m':1,'k':1,'r':1}

        for c in  countA:       #for comparing elements in dict countA
            if countA[c] != countB.get(c, 0):       #get is used to avoid keyword error, 
                return False
        
        return True

res = Solution()        #object creation
a = "mrk"
b ="krm"
print(res.anagram(a, b))


