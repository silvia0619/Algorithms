# 344. Reverse String

# 처음 반과 끝의 반을 바꿔주면 REVERSE 완성!
# RECURSIVE도 똑같이 해줌 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        ############ RECURSIVE SOLUTION (NOT FAST) ###############
        def recursive(left, right, s):
            if left >= right:
                return 
            s[left], s[right] = s[right], s[left]
            recursive(left + 1, right - 1, s)
        recursive(0, len(s) -1, s)
            