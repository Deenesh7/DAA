def isPalindrome(s):
    a = ""
    for ch in s:
        a += ch
    
    s = "".join(reversed(s))
    return s == a

def PalindromicStrings(arr, N):
    for i in range(N):
        if (isPalindrome(arr[i])):
            return arr[i]
    return -1

if __name__ == '__main__':
    arr = ["abc", "car", "ada", "racecar", "cool"]
    N = len(arr)
    
    s = PalindromicStrings(arr, N)
    print(s)
