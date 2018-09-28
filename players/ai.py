from .player import Player


class AI(Player):
    """Class that represents an AI player."""

    def turn(self, board):
        """
        Make a turn.

        The strategy is taken from here: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy

        :param board: the current game's board
        :type board: BoardRepresentation
        :return: choice of player
        :rtype: tuple
        """
        raise NotImplementedError

    def _win(self):
        raise NotImplementedError

    def _block(self):
        raise NotImplementedError

    def _fork(self):
        raise NotImplementedError

    def _block_opponent_fork(self):
        raise NotImplementedError

    def _center(self):
        raise NotImplementedError

    def _opposite_corner(self):
        raise NotImplementedError

    def _empty_corner(self):
        raise NotImplementedError

    def _empty_side(self):
        raise NotImplementedError

    def _first_turn(self):
        raise NotImplementedError
