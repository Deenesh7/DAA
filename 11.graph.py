class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        def countPaths(i, j, step):
            if step > maxMove:
                return 0
            if i < 0 or i >= n or j < 0 or j >= m:
                return 1
            
            if dp[i][j][step] != -1:
                return dp[i][j][step]
            
            left = countPaths(i, j - 1, step + 1)
            right = countPaths(i, j + 1, step + 1)
            down = countPaths(i + 1, j, step + 1)
            up = countPaths(i - 1, j, step + 1)
            
            dp[i][j][step] = (left + right + down + up) % MOD
            return dp[i][j][step]
        
        dp = [[[-1] * (maxMove + 1) for _ in range(m)] for _ in range(n)]
        return countPaths(startRow, startColumn, 0) % MOD
solution = Solution()
n = 2
m = 2
maxMove = 2
startRow = 0
startColumn = 0
print(solution.findPaths(n, m, maxMove, startRow, startColumn))  
