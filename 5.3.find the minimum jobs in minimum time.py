class Solution:
    def minimumTimeRequired(self, jobs, k):
        def fn(i):
            """Assign jobs to workers and find minimum time."""
            nonlocal ans 
            if i == len(jobs):
                ans = min(ans, max(time))
            else: 
                for kk in range(k):
                    if not kk or time[kk-1] != time[kk]:
                        time[kk] += jobs[i]
                        if max(time) < ans:
                            fn(i + 1)
                        time[kk] -= jobs[i]
        
        ans = float('inf')
        time = [0] * k
        fn(0)
        return ans

def test():
    # Built-in input values
    jobs = [3, 2, 3]
    k = 3
    print(f"Jobs: {jobs}")
    print(f"Number of workers: {k}")
    
    solution = Solution()
    result = solution.minimumTimeRequired(jobs, k)
    print("The minimum time required:", result)

if __name__ == "__main__":
    test()
