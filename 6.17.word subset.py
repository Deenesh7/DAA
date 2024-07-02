class Solution:
    def is_subset(self, a, b):
        # Function to check if string a is a subset of string b
        count_a = {}
        count_b = {}
        
        # Count characters in string a
        for char in a:
            if char in count_a:
                count_a[char] += 1
            else:
                count_a[char] = 1
        
        # Count characters in string b
        for char in b:
            if char in count_b:
                count_b[char] += 1
            else:
                count_b[char] = 1
        
        # Check if every character in b is in a with enough count
        for char in count_b:
            if char not in count_a or count_a[char] < count_b[char]:
                return False
        
        return True
    
    def universalStrings(self, words1, words2):
        result = []
        
        # Check each string in words1
        for a in words1:
            is_universal = True
            
            # Check if a is universal for all strings in words2
            for b in words2:
                if not self.is_subset(a, b):
                    is_universal = False
                    break
            
            # If a is universal, add it to the result
            if is_universal:
                result.append(a)
        
        return result

# Example usage:
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
sol = Solution()
print(sol.universalStrings(words1, words2))  # Output: ["facebook", "google", "leetcode"]

words2 = ["l", "e"]
print(sol.universalStrings(words1, words2))  # Output: ["apple", "google", "leetcode"]
