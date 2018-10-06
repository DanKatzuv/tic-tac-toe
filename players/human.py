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
            print(board)
            cell = self._get_user_input(board)
            row, column = cell[0], cell[1]
            if not board.is_cell_empty(row, column):
                print(f'cell number {cell} is not empty')
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
        while True:
            number = input(
                f'Player {self.mark}, enter a cell number between 1 and 9: ')
            try:
                number = int(number)
            except ValueError:
                print('You did not enter a number')
                print(board)
                continue

            if not 0 < number <= 9:
                print(f'Cell {number} is out of bounds')
                print(board)
                continue

            return divmod(number - 1, 3)
