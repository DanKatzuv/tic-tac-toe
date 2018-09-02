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

    def _is_winner(self, row, column):
        for row in self.board:
            if len(set(row)) == 1:
                return True
        for column in self.board:
            if len(set(column)) == 1:
                return True
        main_diagonal = [self.board[i][i] for i in xrange(3)]
        secondary_diagonal = [self.board[i][2 - i] for i in xrange(3)]
        return any(len(set(diagonal)) == 1 for diagonal in (main_diagonal, secondary_diagonal))
    def _raise_if_cell_not_in_bounds(self, row, column):
        try:
            self.board[row][column]
        except IndexError:
            raise NotEmptyCellError(row, column)


class OutOfBoundsError(IndexError):
    def __init__(self, row, column):
        super(IndexError, self).__init__()
        self.row = row
        self.column = column