class Solution:
    def dp(self, i, nums, tr, dct):
        if tr == 0:
            return 1
        if i == 0:
            if tr - nums[i] == 0:
                return 1
            return 0
        if (i, tr) in dct:
            return dct[(i, tr)]
        x = self.dp(i - 1, nums, tr - nums[i], dct)
        y = self.dp(i - 1, nums, tr, dct)
        dct[(i, tr)] = x + y
        return dct[(i, tr)]

    def findTargetSumWays(self, nums, target):
        sm = sum(nums)
        n = len(nums)
        if target > sm:
            return 0
        if (sm - target) % 2:
            return 0
        tr = (sm - target) // 2
        nums.sort()
        dp = [[0] * (tr + 1) for i in range(n)]
        for i in range(n):
            dp[i][0] = 1
        if nums[0] <= tr:
            dp[0][nums[0]] = 1
        for i in range(1, n):
            for j in range(tr + 1):
                x = 0
                if nums[i] <= j:
                    x = dp[i - 1][j - nums[i]]
                y = dp[i - 1][j]
                dp[i][j] = x + y
        zero = nums.count(0)
        if zero:
            return dp[-1][tr] * 2
        return dp[-1][tr]
        # return self.dp(n-1,nums,tr,{})*(2**zero)

# Example input to demonstrate usage
nums = [1]
target = 1
sol = Solution()
print(sol.findTargetSumWays(nums, target))  # Output should be 5
