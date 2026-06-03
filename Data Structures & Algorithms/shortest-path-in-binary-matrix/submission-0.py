class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]==1:
            return -1
            
        ROWS, COLS=len(grid), len(grid[0])

        visited=set()
        path=deque()

        visited.add((0,0))
        path.append((0,0))

        length=1
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        while path:
            for i in range(len(path)):
                r,c=path.popleft()

                for dr,dc in directions:
                    if r+dr==ROWS and c+dc==COLS:
                        return length

                    if min(r+dr,c+dc)<0 or r+dr>=ROWS or c+dc>=COLS or (r+dr,c+dc) in visited or grid[r+dr][c+dc]==1:
                        continue

                    visited.add((r+dr,c+dc))
                    path.append((r+dr,c+dc))
            length+=1
            
        return -1