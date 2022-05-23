# 647. Palindromic Substrings
# 어려워어려워
# 답지봄 https://blog.naver.com/eternalklaus/222629640359
# substring 의 갯수가 odd 인지 even 인지 확인하고 제일 첫 알파벳이랑 끝이 같은지 확인 같지 않다면 다음 char
# 처음과 끝만 확인하는 이유: 그 안에 있는 다른 친구들은 이미 확인 끝남

# example: abcbd
# counter = 0
# n = 5
# when i = 0 
# ODD
# li = 0, ri = 0     # 처음은 항상 true 왜냐면 char 이 하나라서
# li = -1, ri = 1    # li 가 0 보다 작아서 다음
# EVEN
# li = -1, ri = 0    # li 가 0 보자 작아서 다음
# when i = 1
# ODD
# li = 1, ri = 1
# li = 0, ri = 2     # s[li] != s[ri]
# EVEN 
# li = 0, ri = 1     # s[li] != s[ri]
# ...

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        counter = 0
        n = len(s)
        for i in range(n):
            # odd nums
            li, ri = i, i
            while li >= 0 and ri < n and s[li] == s[ri]:
                li, ri = li - 1, ri + 1
                counter += 1
            # even nums
            li, ri = i - 1, i
            while li >= 0 and ri < n and s[li] == s[ri]:
                li, ri = li - 1, ri + 1
                counter += 1
        return counter