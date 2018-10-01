from board.board_representation import BoardRepresentation
from .player import Player


class AI(Player):
    """Class that represents an AI player."""

    def turn(self, board):
        """
        Make a turn.

        The strategy is taken from here: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy.
        Every turn this method runs on the list of available moves. The player should always pick the first possible
        option. So for example, the player should always try to win (duh), but if this is not possible, and the opponent
        can win in the next turn, player should block, and so on.

        Every option is represented as a method. If an option is possible, its corresponding method will return the row
        and column of the player's choice. If an option is not possible, its corresponding method will not return
        anything (or, in fact, will return None). Only when a positive (None is False) result is returned from a
        certain method, will this method return the player's choice.

        :param board: the current game's board
        :type board: BoardRepresentation
        :return: choice of player
        :rtype: tuple
        """
        for move in self.moves:
            result = move(self)
            if result:
                return result

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
    moves = (_first_turn, _second_turn, _win, _block, _fork, _block_opponent_fork,
             _center, _opposite_corner, _empty_corner, _empty_side)

    @staticmethod
    def _all_sequences(board):
        """
        Return all the sequences in a board.

        A "sequence" is defined as every sequence of cells in a tic-tac-toe board, so "all sequences" is all the
        rows, all the columns, the main diagonal and the secondary diagonal.

        :param board: current board
        :type: BoardRepresentation
        :return: all the sequences in the board
        :rtype: list
        """
        sequences = list()
        sequences.append([row for row in board])  # rows
        sequences.append(list(zip(*board)))  # columns
        sequences.append([board[i][i] for i in range(3)])  # main diagonal
        sequences.append([board[i][2 - i]
                          for i in range(3)])  # secondary_diagonal
        return sequences