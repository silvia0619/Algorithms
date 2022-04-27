# 217. Contains Duplicate

# Input: nums = [1,2,3,1]       Output: true
# Input: nums = [1,2,3,4]       Output: false

#  noDupNums = list"(dict.fromkeys(nums))" -> nums의 val을 key 로 가지는 dictionary만들어 (dict은 같은 key가질 수 없기 때문에 dup 자동으로 없어짐 개꿀)
# "noDupNums = list"(dict.fromkeys(nums)) -> 다시 list로 만들어
# 갯수 비교하고 차이나면 dup 있는거자나

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        noDupNums = list(dict.fromkeys(nums))
        if(not len(nums) == len(noDupNums)):
            return True
        return False