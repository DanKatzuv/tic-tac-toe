from itertools import product

from board.board_representation import BoardRepresentation


class Board:
    """Class that represents a tic-tac-toe board."""
    EMPTY = ' '

    def __init__(self):
        """Instantiate a tic-tac-toe board."""
        self._rows = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def __str__(self):
        """
        :return: a string describing the current board
        :rtype: str
        """
        return ''.join(' | '.join(row) + '\n' for row in self._rows)

    @property
    def board(self):
        """
        Return a read-only property of the board.

        :return: the current board
        :rtype: list
        """
        return self._rows[:]

    def representation(self):
        """
        Return representation of the board for a player.

        :return: representation of the current board
        :rtype: BoardRepresentation
        """

        return BoardRepresentation(self._rows)

    def move(self, player, row, column):
        """
        Make one move in the game and return whether a win occurred.
        :param player: current player
        :type player: str
        :param row: row the last mark has been inserted into
        :type row: int
        :param column: column the last mark has been inserted into
        :type column: int
        :return: whether a win occurred
        :rtype: bool
        """
        self._insert(player, row, column)
        return self._has_win_occurred(row, column)

    def is_full(self):
        """
        Return whether the board is full.

        :return: whether the board is full
        :rtype: bool
        """
        return all(not self.is_cell_empty(row, column) for row, column in product(range(3), range(3)))

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
        return self._rows[row][column] == self.EMPTY

    def _insert(self, player, row, column):
        """
        Insert a mark of player into the board.

        :param player: current player
        :type player: str
        :param row: row the last mark has been inserted into
        :type row: int
        :param column: column the last mark has been inserted into
        :type column: int
        """
        self._rows[row][column] = player

    @classmethod
    def _is_win_in_sequence(cls, sequence):
        return cls.EMPTY not in sequence and len(set(sequence)) == 1

    def _has_win_occurred(self, row_number, column_number):
        """
        Return whether a win has occurred.

        :param row_number: row the last mark has been inserted into
        :type row_number: int
        :param column_number: column the last mark has been inserted into
        :type column_number: int
        :return: whether a win has occurred
        :rtype: bool
        """
        sequences = list()
        sequences.append(self._rows[row_number])  # row
        sequences.append([i[column_number] for i in self._rows])  # column
        if row_number == column_number:
            sequences.append([self._rows[i][i]
                              for i in range(3)])  # main diagonal
        if row_number == 2 - column_number:
            sequences.append([self._rows[i][2 - i]
                              for i in range(3)])  # secondary diagonal

        return any(self._is_win_in_sequence(sequence) for sequence in sequences)
