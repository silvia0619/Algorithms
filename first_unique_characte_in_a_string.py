# 387. First Unique Character in a String
# HASH

# frequncy하나 만들어 놓고 그 안에 처음 만난 알파벳이면 char = 1
# 그 다음부터는 하나씩 더 해줘 (a 가 4번 나왔으면 a = 4 / frequency[a] = 4)
# frequency 처음부터 돌면서 제일 처음 1인 친구 return 

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1
        
        
        ########### EXCEED TIME LIMIT ###########
        # for i in s:
        #     newList = list(s)
        #     newList.remove(i)
        #     if not i in newList:
        #         return s.index(i)
        # return -1