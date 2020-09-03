class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board
        
        def backtrack(r):
            if r == n:
                board = generateBoard()
                solution.append(board)
            else:
                for i in range(n):
                    if i in columns or r - i in diagonal1 or r + i in diagonal2:
                        continue
                    queens[r] = i
                    columns.add(i)
                    diagonal1.add(r - i)
                    diagonal2.add(r + i)
                    backtrack(r + 1)
                    columns.remove(i)
                    diagonal1.remove(r - i)
                    diagonal2.remove(r + i)

        solution = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ['.'] * n
        backtrack(0)
        return solution
