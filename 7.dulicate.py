class Solution:
    def uniqueElements(self, nums):
        unique_set = set()
        unique_list = []
        
        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
                unique_list.append(num)
        
        return unique_list

solution = Solution()
input1 = [3, 7, 3, 5, 2, 5, 9, 2]
output1 = solution.uniqueElements(input1)
print(output1)  

