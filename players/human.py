from .player import Player


class Human(Player):
    """Class that represents a human player."""

    def turn(self, board):
        """
        Make a turn.

        :param board: the current game's board
        :type board: Board
        :return: choice of player
        :rtype: tuple
        """
        while True:
            print(board)
            row = self._get_user_input('row')
            column = self._get_user_input('column')

            if not board.is_cell_empty(row, column):
                print(f'The cell at row {row}, column {column} is not empty')
                continue

            return row, column

    def _get_user_input(self, name):
        """
        Get the row or column number the user inputted.

        :param name: the dimension (row or column) the number from the user is desired of
        :type name: str
        :return: the user's choice
        :rtype: int
        """
        while True:
            number = input(f'Player {self.mark}, enter a {name} number between 1 and 3: ')
            try:
                number = int(number)
            except ValueError:
                print('You did not enter a number')

            if not 0 < number <= 3:
                print(f'{name.capitalize()} {number} is out of bounds')
                continue

            return number - 1
