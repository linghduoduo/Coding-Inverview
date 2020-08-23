class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def is_valid(row, col):
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
                return False
            else:
                return True

        def dfs(row, col):
            if not is_valid(row, col):
                return
            if board[row][col] == '.':
                return
            board[row][col] = "."
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)

        if not board:
            return

        battleships = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'X':
                    battleships += 1
                    dfs(row, col)
        return battleships