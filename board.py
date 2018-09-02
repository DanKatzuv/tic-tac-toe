class Board(object):
    EMPTY = ' '

    def __init__(self):
        # self.board = [3 * [' ']]
        self.board = [['X', 'O', 'X'],
                      ['X', 'O', 'X'],
                      ['X', 'O', 'X']]

    def __str__(self):
        return ''.join(' '.join(row) + '\n' for row in self.board)

    def turn(self, player, row, column):
        self._insert(player, row, column)
        return self._is_winner(row, column)

    def _insert(self, player, row, column):
        self._raise_if_cell_not_empty(row, column)
        self.board[row][column] = player