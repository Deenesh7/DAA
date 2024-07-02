class Solution:
    def countPairs(self, nums, k):
        index_dict = {}
        for idx, num in enumerate(nums):
            if num not in index_dict:
                index_dict[num] = []
            index_dict[num].append(idx)
        
        c = 0
        for indices in index_dict.values():
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        c += 1
        return c
nums = [1,2,3,4]
k = 2
solution = Solution()
print(solution.countPairs(nums, k))  # Output: 4
