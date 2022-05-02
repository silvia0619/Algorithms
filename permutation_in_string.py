# 567. Permutation in String
# 답지 조금 봄 sliding window

# s2 처음부터 s1의 갯수 만큼 뒤로 이동 하면서 확인
# s1 에서 찾는 char 이 sub 에 있으면 확인 하고 remove
# sub이 다 remove 돼서 아무거도 안 남아있으면 True
# 아니면 slide window

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        start = 0
        end = len(s1)

        while end <= len(s2):
            sub = list(s2[start:end])  # LIST여야 remove(value) 쓸 수 있음
            for char in s1:
                if char not in sub:
                    start +=1
                    end +=1
                else:
                    sub.remove(char)
                if len(sub) == 0:
                    return True
        return False    