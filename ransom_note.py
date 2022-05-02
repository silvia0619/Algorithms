# 383. Ransom Note

# remove해줘야 하니까 magazine List에 넣어 놓고 
# ransomNote에 필요한 레터 하나씩 magazine에서 remove
# 못 찾으면 return False

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazineList = list(magazine)
        for c in ransomNote:
            if c in magazineList:
                magazineList.remove(c)
            else:
                return False
        return True