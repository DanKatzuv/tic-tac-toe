from player import Player


class Human(Player):
    """Class that represents a human player."""

    def __init__(self, mark):
        """
        Instantiate a human player.

        :param mark: the mark of the player (X, O)
        :type mark: str
        """
        super().__init__(mark)

    def turn(self, board):
        """
        Make a turn.

        :param board: the current game's board
        :type board: Board
        :return: choice of player
        :rtype: tuple
        """
        print(board)
        return self.cell_input()

    def cell_input(self):
        """
        Input a column number from player.

        : param player: player to ask the input for
        : type player: str
        : return: column number player inputted
        : rtype: tuple
        """
        row = int(input(f'Player {self.mark}, enter a row number between 1 and 3: ')) - 1
        column = int(input(f'Player {self.mark}, enter a column number between 1 and 3: ')) - 1
        return row, column
