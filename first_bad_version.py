# 278. First Bad Version
# binary search tree

# 찾는 array의 시작점 끝점 옮기면서 찾기
# mid의 isBadVersion이 false 면 바로 뒤에가 true 인지 확인
# edge case: mid 가 1 이고 isBadVersion(mid)가 ture 면 처음부터 다 true 라서 return 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while(start <= end):
            mid = (end + start) // 2
            if(not isBadVersion(mid)):
                if(isBadVersion(mid + 1)):
                    return mid + 1
                else:
                    start = mid + 1 
            else:
                if(mid == 1):
                    return 1
                end = mid - 1
        