# 557. Reverse Words in a String III
# 답지봄

# **FOR** 아니고 while 써야됨
# 띄어쓰기로 떨어져 있는 단어의 첫번째 = l
# 띄어쓰기로 떨어져 있는 단어의 마지막 = r
# 띄어쓰기 아니면 r하나씩 옮겨주고
# 띄어쓰기면 해당하는 단어 reverse 해 주고 앞에 뒤에 string붙어줘
# r 도 l 도 띄어쓰기 바로 다음 char index지정

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        r = 0
        while r < len(s):
            while r < len(s) and s[r] != ' ':
                r += 1
            s = s[:l] + s[l:r][::-1] + s[r:]    # 해당하는 단어는 reverse 앞과 뒤는 ++
            r += 1
            l = r
        return s