# 3. Longest Substring Without Repeating Characters
# sliding window

# start 랑 end 정해놓고 substring하는데 같은 알파벳 들어있으면 "(list(dict.fromkeys(sub)))" 이거로 확인해서 
# start하나 더해주고 아니면 end 하나 더 해주고 
# end 늘일때는 maxLength 도 같이 늘어나니까 max 업데이트

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        maxLength = 0
        while end <= len(s):
            sub = s[start:end] 
            if not len(sub) == len(list(dict.fromkeys(sub))):
                start += 1
            else:
                end += 1
                if maxLength < len(sub):
                    maxLength = len(sub)
        return maxLength