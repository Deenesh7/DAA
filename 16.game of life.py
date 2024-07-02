class Solution:
    def gameOfLife(self, board):
        direct = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def num_of_live(board, x, y):
            count = 0
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] > 0:
                    count += 1
            return count
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = num_of_live(board, i, j)
                if board[i][j] >= 1:
                    if num < 2 or num > 3:
                        board[i][j] = 2  
                else:
                    if num == 3:
                        board[i][j] = -1 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1

solution = Solution()
board = [
    [0],
]
solution.gameOfLife(board)
for row in board:
    print(row)
