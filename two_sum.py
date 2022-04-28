# 1. Two Sum

# for loop 두번 돌려서 혹시 같은 index에 있는거 아니면 두개 합 비교 타겟이랑 같으면 return
# BETTER SOLUTION: 
# dic에 target - nums[i] 있는지 봐
# 없으면 하나씩 dic에 넣어줘 근데 자기 자신은 두번 더 할 수 없으니까 하나씩 뒤에 더해줘
# dic에 저장 할때는 val: index 이렇게 저장해줘 나중에 index 찾을 수 있게

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if not i == j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return -1
    
        # BETTER SOLUTION  
        dic={}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i
            