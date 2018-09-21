from random import choice

from board import Board
from player import Player


class RandomComputer(Player):
    """Class that represents a random computer player."""

    def __init__(self, mark):
        """
        Instantiate a random computer player.

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

        vacant_cells = list()
        for row in range(3):
            for column in range(3):
                if board.is_cell_empty(row, column):
                    vacant_cells.append((row, column))

        return choice(vacant_cells)
