class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color=image[sr][sc]
        if orig_color==color:
            return image
        
        rows=len(image)
        cols=len(image[0])
        
        def dfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or image[r][c]!=orig_color:
                return

            image[r][c]=color
        
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)
        return image
