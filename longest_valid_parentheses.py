# 32. Longest Valid Parentheses
# HARD 넘무 어려워

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        invalid = []
        valid = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                invalid.append(i)
            else:
                if len(invalid) > 0:
                    valid[invalid.pop()] = 1
                    valid[i] = 1                        # 모든 valid 한 parentheses index에 1 넣어주기
        counter = 0
        maxValid = 0 
        for i in valid:                             
            if i == 1:                                  # 가장 길게 1 이 연속되는 숫자 찾기
                counter += 1
                maxValid = max(counter, maxValid)
            else:
                counter = 0
        return maxValid
        