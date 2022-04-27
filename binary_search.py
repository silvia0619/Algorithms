# 704. Binary Search
# binary tree search

# 어디서 찾을지 정하기 array 의 시작 & 끝 계속 줄이면서 찾기

# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. 
# Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while(start <= end):
            if(nums[(start + end)//2] == target):
                return (start + end) //2
            elif(nums[(start + end)//2] > target):
                end = (start + end)//2 - 1
            else:
                start = (start + end)//2 + 1
        return -1