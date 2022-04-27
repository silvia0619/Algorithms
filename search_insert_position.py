# 35. Search Insert Position
# binary search tree

# 찾는 array의 시작점 끝점 옮기면서 찾기
# target   <     target   <    target    <      target    <      target
#                nums[i]                       nums[i+1]
# nums[i]랑 target 이 같을때
# nums[i]보다 target 이 더 클 때 -> nums[i + 1] 있는데 target보다 크거나 같으면 return mid + 1 OR start 옮겨주고
#                               -> nums[i + 1] 없으면 target이 제일 크다!
# nums[i] 보다 target 이 더 작으면 end 옮겨주는데 "혹시 mid가 0 이면 target이 제일 작은거야"

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = (start + end)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                if(mid + 1 <= len(nums) - 1):
                    if(nums[mid + 1] >= target):
                        return mid + 1
                    else:
                        start = mid + 1
                else:
                    return len(nums)
            else:
                if(mid == 0):
                    return 0
                end = mid - 1