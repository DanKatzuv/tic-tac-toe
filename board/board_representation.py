class BoardRepresentation:
    """
    Class that represents a read-only board for a player.

    This class is used for the players to get a view of the board
    without having the ability to change it on their own.
    """

    def __init__(self, rows):
        """Instantiate a tic-tac-toe board representation.

        :param rows: the current board
        :type rows: list
        """
        self._rows = rows

    def __str__(self):
        """
        :return: a string describing the current board
        :rtype: str
        """
        return ''.join(' | '.join(row) + '\n' for row in self._rows)

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
        return self._rows[row][column] == ' '

    @property
    def rows(self):
        """
        :return: rows of the board
        :rtype: list[list]
        """
        return self._rows

    @property
    def columns(self):
        """
        :return: columns of the board
        :rtype: list[list]
        """
        return list(zip(*self._rows))

    @property
    def main_diagonal(self):
        """
        :return: main diagonal of the board.
        :rtype: list
        """
        return [self._rows[row][row] for row in range(3)]

    @property
    def secondary_diagonal(self):
        """
        :return: main diagonal of the board.
        :rtype: list
        """
        return [self._rows[row][2 - row] for row in range(3)]
