# 242. Valid Anagram

# 두 스트링 다 sort 해 주고 같으면 True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False
        