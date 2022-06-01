# 1480. Running Sum of 1d Array

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in range(len(nums)):
            nums[i] += temp
            temp = nums[i]
        return nums