class Solution(object):
   def fourSumCount(self, A, B, C, D):
      sums ={}
      for i in A:
         for j in B:
            if i+j not in sums:
               sums[i+j] = 1
            else:
               sums[i+j] +=1
      counter = 0
      for i in C:
         for j in D:
            if -1 * (i+j) in sums:
               #print(-1 * (i+j))
               counter+=sums[-1*(i+j)]
      return counter
ob1 = Solution()
print(ob1.fourSumCount([1, 2], [-2, -1],  [-1, 2],  [0, 2]))
