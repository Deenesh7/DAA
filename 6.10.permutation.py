class Solution:
    def permuteUnique(self, nums):
        ans = []
        nums.sort()
        
        def subset(p, up):
            if len(up) == 0:
                if p not in ans:
                    ans.append(p)
                return 
            ch = up[0]
            for i in range(len(p) + 1):
                subset(p[0:i] + [ch] + p[i:], up[1:])
                
        subset([], nums)
        return ans

# Example input to demonstrate usage
nums = [1, 1, 2]
sol = Solution()
print(sol.permuteUnique(nums))  # Expected output should be [[1, 1, 2], [1, 2, 1],
