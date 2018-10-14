from itertools import cycle
from random import randint

from board.board import Board


class Game:
    """Class that represents a tic-tac-toe game."""
    FIRST_PLAYER_MARK = 'X'
    SECOND_PLAYER_MARK = 'O'

    def __init__(self, player_x_type, player_o_type):
        """Instantiate a tic-tac-toe game.

        :param player_x_type: type of the first player (player x)
        :type player_x_type: Player
        :param player_o_type: type of the second player (player o)
        :type player_o_type: Player
        """
        self.board = Board()
        self.player_x = player_x_type(self.FIRST_PLAYER_MARK)
        self.player_o = player_o_type(self.SECOND_PLAYER_MARK)

    def play(self):
        """Main method running the game."""
        for player in cycle((self.player_x, self.player_o)):
            if self._turn(player):
                return

    def _turn(self, player):
        """
        Method running every turn and returns whether the game has ended.

        :param player: the current player
        :type player: Player
        :return: whether the game has ended
        :rtype: bool
        """
        row, column = player.turn(self.board.representation())
        if self.board.move(player.mark, row, column):
            print(self.board)
            print(f'Player {player.mark} has won! :-)')
            return True

        if self.board.is_full():
            print(self.board)
            print('Board is full, tie.')
            return True

        return False
