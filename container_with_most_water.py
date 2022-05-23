# 11. Container With Most Water

# start 랑 end 정해놓고 부피 구하고 제일크면 업데이트 아니면 놔두고
# start 랑 end 중에 짧은 쪽을 한칸 옮기기

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            newMaxWater = (end - start) * min(height[start], height[end])
            if maxWater < newMaxWater:
                maxWater = newMaxWater
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxWater