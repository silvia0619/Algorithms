# 733. Flood Fill
# 완전히 답지 봤어

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        color = image[sr][sc] 
        if color == newColor: 
            return image                    # edge case if color == new Color
        def dfs(r, c):          
            if image[r][c] == color:        # 현재 받은 pixel에 있는 color확인하고
                image[r][c] = newColor      # 같으면 set newColor
                if r >= 1: dfs(r-1, c)      # right
                if r+1 < row: dfs(r+1, c)   # left
                if c >= 1: dfs(r, c-1)      # up
                if c+1 < col: dfs(r, c+1)   # down
        dfs(sr, sc)
        return image