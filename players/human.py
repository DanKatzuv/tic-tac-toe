from itertools import product

from .player import Player


class Human(Player):
    """Class that represents a human player."""

    def turn(self, board):
        """
        Make a turn.

        :param board: the current game's board
        :type board: BoardRepresentation
        :return: choice of player
        :rtype: tuple
        """

        while True:
            new_board = self._new_board(board)
            print(new_board)
            cell = self._get_user_input(board)
            row, column = cell[0], cell[1]
            if not board.is_cell_empty(row, column):
                print(f'cell number {row * 3 + column + 1} is not empty')
                continue

            return row, column

    def _get_user_input(self, board):
        """
        Get the row or column number the user inputted.

        :param board: the current board
        :type board: BoardRepresentation
        :return: the user's choice
        :rtype: tuple
        """
        new_board = self._new_board(board)
        while True:
            number = input(f'Player {self.mark}, enter a cell number between 1 and 9: ')
            try:
                number = int(number)
            except ValueError:
                print('You did not enter a number')
                print(new_board)
                continue

            if not 0 < number <= 9:
                print(f'Cell {number} is out of bounds')
                print(new_board)
                continue

            return divmod(number - 1, 3)

    @staticmethod
    def _new_board(board):
        """
        :param board: current board
        :type board: BoardRepresentation
        :return: a more convenient board representation for a human
        :rtype: list[list]
        """
        new_board = [['', '', ''],
                     ['', '', ''],
                     ['', '', '']]
        for row, column in product(range(3), range(3)):
            if board.is_cell_empty(row, column):
                to_insert = str(row * 3 + column + 1)
            else:
                to_insert = board.rows[row][column]
            new_board[row][column] = to_insert
        return ''.join(' | '.join(row) + '\n' for row in new_board)
