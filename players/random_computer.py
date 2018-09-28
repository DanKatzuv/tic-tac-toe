from itertools import product
from random import choice

from .player import Player


class RandomComputer(Player):
    """Class that represents a random computer player."""

    def turn(self, board):
        """
        Make a turn.

        :param board: the current game's board
        :type board: BoardRepresentation
        :return: choice of player
        :rtype: tuple
        """
        return choice([(row, column) for row, column in product(
            range(3), range(3)) if board.is_cell_empty(row, column)])
