from board import board


class BoardRepresentation:
    """
    Class that represents a read-only board for a player.

    This class is used for the players to get a view of the board
    without having the ability to change it on their own.
    """

    def __init__(self, board):
        """Instantiate a tic-tac-toe board represetation.

        :param board: the current board
        :type board: Board
        """
        self.board = board.board

    def __str__(self):
        """
        :return: a string describing the current board
        :rtype: str
        """
        return ''.join(' | '.join(row) + '\n' for row in self.board)

    def is_cell_empty(self, row, column):
        """
        Return whether a certain cell is empty.

        :param row: row number of the checked cell
        :type row: int
        :param column: column number of the checked cell
        :type column: int
        :return: whether a certain cell is empty
        :rtype: bool
        """
        return self.board[row][column] == board.Board.EMPTY

    def __getitem__(self, row):
        return self.board[row]
