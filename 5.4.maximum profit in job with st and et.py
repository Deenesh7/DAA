class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        ind = 0
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            startTime[ind] = s
            endTime[ind] = e
            profit[ind] = p
            ind += 1
        
        n = len(profit)
        dp = [0] * n
        dp[0] = profit[0]

        def find_last_non_conflicting(j):
            lo, hi = 0, j - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if endTime[mid] <= startTime[j]:
                    if endTime[mid + 1] <= startTime[j]:
                        lo = mid + 1
                    else:
                        return mid
                else:
                    hi = mid - 1
            return -1

        for i in range(1, n):
            incl_prof = profit[i]
            l = find_last_non_conflicting(i)
            if l != -1:
                incl_prof += dp[l]
            dp[i] = max(incl_prof, dp[i - 1])

        return dp[-1]

def test():
    # Built-in input values
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(f"Start times: {startTime}")
    print(f"End times: {endTime}")
    print(f"Profits: {profit}")
    
    solution = Solution()
    result = solution.jobScheduling(startTime, endTime, profit)
    print("The maximum profit:", result)

if __name__ == "__main__":
    test()
