# 1461. Check If a String Contains All Binary Codes of Size K
# 답지봄

# Input: s = "00110110", k = 2 일때
# 00, 01, 11, 10, 01, 11, 10 를 확인하고 codes 에 없으면 추가

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        codes = set()
        for i in range(len(s) - k + 1):         
            codes.add(s[i:i+k])                 # s 의 substring k 개 만큼이 set에 없으면 추가 있으면 건너뛰기
        return len(codes) == 2 ** k             # set 의 갯수가 2 의 k 승 만큼 있으면 return true