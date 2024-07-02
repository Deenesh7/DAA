class Solution:
    def combinationSum(self, candidates, target):
        self.res = set()
        self.candidates = candidates
        self.targetSum = target
        for i, num in enumerate(candidates):
            self.backtrack([num], i, num)
        return [list(tup) for tup in self.res]

    def backtrack(self, path, i, currentSum):
        if currentSum >= self.targetSum:
            if currentSum == self.targetSum:
                pathTup = tuple(path)
                if pathTup not in self.res:
                    self.res.add(pathTup)
            return
        for j in range(i, len(self.candidates)):
            num = self.candidates[j]
            path.append(num)
            self.backtrack(path, j, currentSum + num)
            path.pop()

# Example input to demonstrate usage
candidates = [2, 3, 6, 7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))  # Expected output should be [[2, 2, 3], [7]]
