class Board(object):
    EMPTY = ' '

    def __init__(self):
        # self.board = [3 * [' ']]
        self.board = [['X', 'O', 'X'],
                      ['X', 'O', 'X'],
                      ['X', 'O', 'X']]

    def __str__(self):
        return ''.join(' '.join(row) + '\n' for row in self.board)
