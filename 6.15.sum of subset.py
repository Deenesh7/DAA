def findSubsets(nums, n):
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset.append(nums[j])
        print(subset)

# Driver Code
arr = [1, 2, 3]
n = len(arr)
findSubsets(arr, n)
