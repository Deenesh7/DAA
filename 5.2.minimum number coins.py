class Solution:
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        
        extraCoins = reachable = 0
        for coin in coins:
            while reachable < (coin - 1):
                reachable = 2 * reachable + 1
                extraCoins += 1
            reachable += coin
        
        while reachable < target:
            reachable = 2 * reachable + 1
            extraCoins += 1 
        
        return extraCoins

def test():
    # Built-in input values
    coins = [1, 4, 10, 5, 7, 19]
    target = 19
    print(f"Coins: {coins}")
    print(f"Target: {target}")
    
    solution = Solution()
    result = solution.minimumAddedCoins(coins, target)
    print("The minimum number of coins to be added:", result)

if __name__ == "__main__":
    test()
