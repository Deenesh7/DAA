class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        stack = []
        ans = []

        def com2(ind, target):
            if target == 0:
                ans.append(stack[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] <= target:
                    stack.append(candidates[i])
                    com2(i + 1, target - candidates[i])
                    stack.pop()
                else:
                    break

        com2(0, target)
        return ans

# Example input to demonstrate usage
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))  # Expected output should be [[1, 1, 6], [1, 
