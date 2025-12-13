# Given an array arr[] consisting of n integers, find all the array elements which occurs more than floor(n/3) times.
# Note: The returned array of majority elements should be sorted.

# Boyer-Moore’s Voting Algorithm
# steps:
# 1> initialise the ele1, ele2 = 0,  and cnt1, cnt2 = 0
# 2> if ele(1 | 2) is same increment the cnt(1 | 2) if cnt(1 | 2) == 0 then ele(1 | 2) = element
# 3> if element != ele(1 | 2) then decrease the cnts, then append ele1 and 2 in res
# 4> check  both ele1 and ele2 are n=more than n/3, then take 2 majority elements sort them

class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        ele1, ele2 = -1, -1
        cnt1,  cnt2 = 0, 0 
        
        for i in range(0, n, 1):
            if(arr[i] == ele1):
                cnt1 += 1
            
            elif(arr[i] == ele2):
                cnt2 += 1
                
            elif cnt1 == 0:
                ele1 = arr[i]
                cnt1 += 1
            
            elif cnt2 == 0:
                ele2 = arr[i]
                cnt2 += 1
            
            
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []
        cnt1, cnt2 = 0, 0
        
        for i in range(0, n, 1):
            if ele1 == arr[i]:
                cnt1 += 1
            
            if ele2 == arr[i]:
                cnt2 += 1
        
        if cnt1 > n/3:
            res.append(ele1)
        
        if cnt2 > n/3 and ele1 != ele2:
            res.append(ele2)
        
        if(len(res) == 2 and res[0] > res[1]):
            res[0], res[1] = res[1], res[0]
        
        return res


if __name__ == "__main__":
    arr = [2, 2, 3, 1, 1, 1]
    obj = Solution()
    res = obj.findMajority(arr)

    for ele in res:
        print(ele, end=" ")