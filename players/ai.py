from itertools import product
from random import choice

from board.board import Board
from board.board_representation import BoardRepresentation
from game import Game
from .player import Player


class AI(Player):
    """Class that represents an AI player."""

    def turn(self, board):
        """
        Make a turn.

        The strategy is taken from here: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy.
        Every turn this method runs on the list of available moves. The player should always pick the first possible
        option. So for example, the player should always try to win (duh 😜), but if this is not possible, and the
        opponent can win in the next turn, player should block, and so on.

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
            result = move(self, board)
            if result:
                return result

    def _win(self, board):
        """
        Method for handling Rule 1: Win.
    
        Win: If the player has two in a row, they can place a third to get three in a row.
    
        :type board: BoardRepresentation
        :param board: current board
        :return: choice according to Rule 1 if possible
        :rtype: tuple
        """
        return self._win_and_block(board, self.mark)
        
    def _block(self, board):
        """
        Method for handling Rule 2: Block.
    
        Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    
        :type board: BoardRepresentation
        :param board: current board
        :return: choice according to Rule 2 if possible
        :rtype: tuple
        """
        return self._win_and_block(board, self.other_mark())

    @classmethod
    def _win_and_block(cls, board, mark):
        for row_number, row in enumerate(board.rows):
            if cls._is_almost_full(row, mark):
                return row_number, row.index(Board.EMPTY)

        for column_number, column in enumerate(board.columns):
            if cls._is_almost_full(column, mark):
                return column.index(Board.EMPTY), column_number

        main_diagonal = board.main_diagonal
        if cls._is_almost_full(main_diagonal, mark):
            empty = main_diagonal.index(Board.EMPTY)
            return empty, empty

        secondary_diagonal = board.secondary_diagonal
        if cls._is_almost_full(secondary_diagonal, mark):
            empty = secondary_diagonal.index(Board.EMPTY)
            return empty, 2 - empty

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

    def _first_turn(self, board):
        """
        Method that returns the choice of the case when the AI player plays the first turn.

        Playing the corner is the best opening move for the first player.

        :param board: current board
        :type board: BoardRepresentation
        :return: the choice of the first turn
        :rtype: tuple
        """
        if self._number_of_empty_cells(board) == 9:
            return choice((0, 2)), choice((0, 2))

    def _second_turn(self, board):
        """
        Method that returns the choice of the case when the AI player plays the first turn.

        The second player, who shall be designated "O", must respond to X's opening mark in such a way as to avoid
        the forced win. Player O must always respond to a corner opening with a center mark, and to a center opening
        with a corner mark. An edge opening must be answered either with a center mark, a corner mark next to the X,
        or an edge mark opposite the X. Any other responses will allow X to force the win. Once the opening is
        completed, O's task is to follow the above list of priorities in order to force the draw, or else to gain a
        win if X makes a weak play.

        More detailedly, to guarantee a draw, O should adopt the following strategies:
        * If X plays corner opening move, O should take center, and then an edge, forcing X to block in the next
        move. This will stop any forks from happening. When both X and O are perfect players and X chooses to start
        by marking a corner, O takes the center, and X takes the corner opposite the original. In that case,
        O is free to choose any edge as its second move. However, if X is not a perfect player and has played a
        corner and then an edge, O should not play the opposite edge as its second move, because then X is not forced
        to block in the next move and can fork.
        * If X plays edge opening move, O should take center or one of the
        corners adjacent to X, and then follow the above list of priorities, mainly paying attention to block forks.
        * If X plays center opening move, O should take corner, and then follow the above list of priorities,
        mainly paying attention to block forks.

        :param board: current board
        :type board: BoardRepresentation
        :return: the choice of the first turn
        :rtype: tuple
        """

        if self._number_of_empty_cells(board) == 8:
            if not all((board.is_cell_empty(row, column) for row, column in  # if a corner opening occurred,
                        product((0, 2), (0, 2)))):
                return 1, 1  # fill the center
            if not board.is_cell_empty(1, 1):  # if a center opening occured,
                return choice((0, 2)), choice((0, 2))  # fill one of the corners

            for row_number, row in enumerate(board.rows):  # if an edge opening occurred, find location of inserted mark
                if Game.FIRST_PLAYER_MARK in row:
                    first_row, first_column = row, row.find(Game.FIRST_PLAYER_MARK)

            choices = [(1, 1)]  # choices available if edge opening occurred
            for dimension in (first_row, first_column):
                if dimension in (1, 3):
                    choices.append((dimension + 1, 1))
                    choices.append((dimension - 1, 1))

            return choice(choices)

    moves = (_first_turn, _second_turn, _win, _block, _fork, _block_opponent_fork,
             _center, _opposite_corner, _empty_corner, _empty_side)

    @staticmethod
    def _number_of_empty_cells(board):
        """
        Return the number of the empty cells in the board.

        :param board: current board
        :type board: BoardRepresentation
        :return: number of empty cells in board
        :rtype: int
        """
        return sum(1 for row, column in product(range(3), range(3)) if board.rows[row][column] == Board.EMPTY)

    @staticmethod
    def _is_almost_full(sequence, mark):
        """
        Return whether sequence is "almost-full".

        An "almost-full" sequence is a sequence that includes two cells with the same mark and another empty cell.

        :param sequence: sequence for checking whether it is "almost-full"
        :type sequence: list
        :param mark: mark for checking whether there are two cells in sequence of that mark
        :type mark: str
        :return: whether sequence is "almost-full"
        :rtype: bool
        """
        return sequence.count(mark) == 2 and sequence.count(Board.EMPTY) == 1

    def other_mark(self):
        """
        Return the other player's mark.

        :return: mark of the other player
        :rtype: str
        """
        return Game.FIRST_PLAYER_MARK if self.mark == Game.SECOND_PLAYER_MARK else Game.SECOND_PLAYER_MARK
