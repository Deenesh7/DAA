class Solution:
    def maxCoins(self, piles):
        piles.sort(reverse=True)  # Sort piles in descending order
        max_coins = 0
        for i in range(1, len(piles) * 2 // 3, 2):  # Iterate to select your coins
            max_coins += piles[i]
        return max_coins

def read_input():
    input_str = input("Enter the piles of coins separated by spaces: ")
    piles = list(map(int, input_str.split()))
    return piles

if __name__ == "__main__":
    piles = read_input()
    solution = Solution()
    result = solution.maxCoins(piles)
    print("The maximum coins you can get:", result)

