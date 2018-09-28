from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract class that represents a player."""

    def __init__(self, mark):
        """
        Instantiate a player.

        :param mark: the mark of the player (X, O)
        :type mark: str
        """
        self.mark = mark

    @abstractmethod
    def turn(self, board):
        """
        Make a turn.

        :param board: the current game's board
        :type board: BoardRepresentation
        :return: choice of player
        :rtype: tuple
        """
        pass
