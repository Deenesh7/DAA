class Solution:
    def largeGroupPositions(self, s: str) -> list:
        res = []
        i = 0
        j = 1
        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
            j += 1
        return res

# Example usage:
solution = Solution()
s = "abbxxxxzzy"
print(solution.largeGroupPositions(s))  # Expected output: [[3, 6]]
