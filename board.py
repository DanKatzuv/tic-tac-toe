class Board(object):
    EMPTY = ' '

    def __init__(self):
        # self.board = [3 * [' ']]
        self.board = [['X', 'O', 'X'],
                      ['X', 'O', 'X'],
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def __str__(self):
        return ''.join(' '.join(row) + '\n' for row in self.board)

    def turn(self, player, row, column):
        self._insert(player, row, column)
        return self._is_winner(row, column)
    def is_full(self):
        return all(self.EMPTY not in row for row in self.board)

    def _insert(self, player, row, column):
        self._raise_if_cell_not_empty(row, column)
        self.board[row][column] = player

    def _has_win_occurred(self, row, column):
        for row in self.board:
            if len(set(row)) == 1:
                return True
        if len(set(self.board[row])) == 1:
            return True
        if len(set(self.board[column])) == 1:
            return True
        if row == column:
            if len(set([self.board[i][i] for i in range(2)])) == 1:
                return True
        if row == 2 - column:
            if len(set([self.board[i][2 - i] for i in range(2)])) == 1:
                return True
        return False

    def _raise_if_cell_full(self, row, column):
        if self.board[row][column] != self.EMPTY:
            raise FullCellError(row, column)

    def _raise_if_cell_not_in_bounds(self, row, column):
        try:
            self.board[row][column]
        except IndexError:
            raise NotEmptyCellError(row, column)
        if self.board[row][column] != self.EMPTY:
            raise OutOfBoundsError(row, column)


class OutOfBoundsError(IndexError):
    def __init__(self, row, column):
        super(IndexError, self).__init__()
        super().__init__()
        self.row = row
        self.column = column


class FullCellError(Exception):
    def __init__(self, row, column):
        super(NotEmptyCellError, self).__init__()
        super().__init__()
        self.row = row
        self.column = column


def main():
    board = Board()
    print board


if __name__ == '__main__':
    main()
