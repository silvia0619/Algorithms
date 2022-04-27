# 53. Maximum Subarray 
# 답지봤다

# Sum에 - value아니면 다 더한다 혹시 - 면 0 으로 reset해줌
# negative value 더하지 않겠다.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSubSum = nums[0]
        currSubSum = 0
        
        for i in nums:
            if(currSubSum < 0):
                currSubSum = 0
            currSubSum += i
            maxSubSum = max(maxSubSum, currSubSum)
            
        return maxSubSum
                
        