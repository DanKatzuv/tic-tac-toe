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
            row = int(input(f'Player {self.mark}, enter a row number between 1 and 3: ')) - 1
            column = int(input(f'Player {self.mark}, enter a column number between 1 and 3: ')) - 1

            if not board.is_cell_empty(row, column):
                print(f'The cell at row {row}, column {column} is not empty')
                continue
            if not (0 <= row < 3 or 0 <= column < 3):
                print(f'The cell at row {row}, column {column} is out of bounds')
                continue
            return row, column
