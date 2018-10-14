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
        return self._win_and_block(board, self._other_mark())

    @classmethod
    def _win_and_block(cls, board, mark):
        for row_number, row in enumerate(board.rows):
            if cls._is_almost_full(row, mark, Board.EMPTY):
                return row_number, row.index(Board.EMPTY)

        for column_number, column in enumerate(board.columns):
            if cls._is_almost_full(column, mark, Board.EMPTY):
                return column.index(Board.EMPTY), column_number

        main_diagonal = board.main_diagonal
        if cls._is_almost_full(main_diagonal, mark, Board.EMPTY):
            empty = main_diagonal.index(Board.EMPTY)
            return empty, empty

        secondary_diagonal = board.secondary_diagonal
        if cls._is_almost_full(secondary_diagonal, mark, Board.EMPTY):
            empty = secondary_diagonal.index(Board.EMPTY)
            return empty, 2 - empty

    def _fork(self, board):
        """
        Return the choice according to Rule 3: Fork.

        Fork: Create an opportunity where the player has two threats to win (two non-blocked lines of 2).

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 3 if possible
        :rtype: tuple
        """
        sequences = set()
        for sequence in board.all_sequences_coordinates():
            for row, column in sequence:
                if board.rows[row][column] == self.mark:
                    sequences.add(tuple(sequence))
                    continue

        for sequence in sequences:
            for sequence1 in sequences:
                if sequence != sequence1:
                    intersection = set(sequence) & set(sequence1)
                    for row, column in intersection:
                        if board.is_cell_empty(row, column):
                            return row, column

    def _available_winning_combos(self, board):
        """
        :param board: current board
        :type board: BoardRepresentation
        :return: all the cells that if they will be filled, a row of two will be created
        :rtype: list
        """
        available = list()
        for row_number, row in enumerate(board.rows):
            if self._is_almost_full(row, Board.EMPTY, self.mark):
                full = row.index(self.mark)
                available.extend([(row_number, column_number) for column_number in range(3) if column_number != full])

        for column_number, column in enumerate(board.columns):
            if self._is_almost_full(column, Board.EMPTY, self.mark):
                full = column.index(self.mark)
                available.extend([(row_number, column_number) for row_number in range(3) if row_number != full])

        main_diagonal = board.main_diagonal
        if self._is_almost_full(main_diagonal, Board.EMPTY, self.mark):
            full = main_diagonal.index(self.mark)
            available.extend([(cell, cell) for cell in range(3) if cell != full])

        secondary_diagonal = board.secondary_diagonal
        if self._is_almost_full(secondary_diagonal, Board.EMPTY, self.mark):
            full = secondary_diagonal.index(self.mark)
            available.extend([(cell, 2 - cell) for cell in range(3) if cell != full])

        return available

    def _block_fork(self, board):
        """
        Return the choice according to Rule 4: Blocking an opponent's fork.

        Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it.
        Otherwise, the player should block any forks in any way that simultaneously allows them to create two in a
        row. Otherwise, the player should create a two in a row to force the opponent into defending, as long as it
        doesn't result in them creating a fork. For example, if "X" has two opposite corners and "O" has the center,
        "O" must not play a corner in order to win. (Playing a corner in this scenario creates a fork for "X" to win.)

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 4 if possible
        :rtype: tuple
        """
        other_mark = self._other_mark()
        sequences = set()
        for sequence in board.all_sequences_coordinates():
            for row, column in sequence:
                if board.rows[row][column] == other_mark:
                    sequences.add(tuple(sequence))
                    continue

        combos = self._available_winning_combos(board)
        best = list()
        better = list()
        for sequence, sequence1 in product(sequences, sequences):
            if sequence != sequence1:
                intersection = set(sequence) & set(sequence1)
                for row, column in intersection:
                    if board.is_cell_empty(row, column):
                        if (row, column) in combos:
                            best.append((row, column))
                        else:
                            better.append((row, column))
        if len(best) > 0:
            return choice(best)
        if len(better) > 0:
            return choice(better)
        return choice(combos)

    @staticmethod
    def _center(board):
        """
        Return the choice according to Rule 5: Center.

        Center: A player marks the center. (If it is the first move of the game, playing on a corner gives the second
        player more opportunities to make a mistake and may therefore be the better choice; however, it makes no
        difference between perfect players.)

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 5 if possible
        :rtype: tuple
        """
        if board.is_cell_empty(1, 1):
            return 1, 1

    def _opposite_corner(self, board):
        """
        Return the choice according to Rule 6: Opposite corner.

        Opposite corner: If the opponent is in the corner, the player plays the opposite corner.

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 6 if possible
        :rtype: tuple
        """

        def empty_opposite_full(row1, column1, row2, column2):
            """
            :param row1: row of a corner
            :type row1: int
            :param column1: column of a corner
            :type column1: int
            :param row2: row of the opposite corner
            :type row2: int
            :param column2: column of the opposite corner
            :type column2: int
            :return: whether it is possible to make a choice according to Rule 6
            """
            return board.rows[row1][column1] == self._other_mark() and board.is_cell_empty(row2, column2)

        if empty_opposite_full(0, 0, 2, 2):
            return 2, 2
        if empty_opposite_full(0, 2, 2, 0):
            return 2, 0
        if empty_opposite_full(2, 2, 0, 0):
            return 0, 0
        if empty_opposite_full(2, 0, 0, 2):
            return 0, 2

    @staticmethod
    def _empty_corner(board):
        """
        Return the choice according to Rule 7: Empty corner.

        Empty corner: The player plays in a corner square.

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 7 if possible
        :rtype: tuple
        """
        empty_corners = list()
        for corner in board.corners:
            if board.is_cell_empty(*corner):
                empty_corners.append(corner)

        if empty_corners:
            return choice(empty_corners)

    @staticmethod
    def _empty_edge(board):
        """
        Return the choice according to Rule 8: Empty side.

        Empty side: The player plays in a middle square on any of the 4 sides.

        :param board: current board
        :type board: BoardRepresentation
        :return: choice according to Rule 8 if possible
        :rtype: tuple
        """
        empty_edges = list()
        for edge in board.edges:
            if board.is_cell_empty(*edge):
                empty_edges.append(edge)

        if empty_edges:
            return choice(empty_edges)

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
            if not board.is_cell_empty(1, 1):  # if a center opening occurred,
                return choice((0, 2)), choice((0, 2))  # fill one of the corners

            for row_number, row in enumerate(board.rows):  # if an edge opening occurred, find location of inserted mark
                if Game.FIRST_PLAYER_MARK in row:
                    first_row, first_column = row, row.index(Game.FIRST_PLAYER_MARK)

            choices = [(1, 1)]  # choices available if edge opening occurred
            for dimension in (first_row, first_column):
                if dimension in (1, 3):
                    choices.append((dimension + 1, 1))
                    choices.append((dimension - 1, 1))

            return choice(choices)

    moves = (_first_turn, _second_turn, _win, _block, _fork, _block_fork,
             _center, _opposite_corner, _empty_corner, _empty_edge)

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
    def _is_almost_full(sequence, main_char, secondary_char, main_times=2, secondary_times=1):
        """
        Return whether :sequence: is "almost-full".

        An "almost-full" sequence is a sequence that includes :main_times: cell(s) with the :main_char: and other
        :secondary_times: cell(s) with :secondary_char:.
        :main_char
        :param sequence: sequence to be checked
        :type sequence: list
        :param main_char: character that should appear twice
        :type main_char: str
        :param secondary_char: character that should appear once
        :type secondary_char: str
        :param main_times: amount of times :main_char: should appear
        :type main_times: int
        :param secondary_times: amount of times :secondary_char: should appear
        :type secondary_times: int
        :return: whether :sequence: is "almost-full"
        """
        return sequence.count(main_char) == main_times and sequence.count(secondary_char) == secondary_times

    def _other_mark(self):
        """
        Return the other player's mark.

        :return: mark of the other player
        :rtype: str
        """
        return Game.FIRST_PLAYER_MARK if self.mark == Game.SECOND_PLAYER_MARK else Game.SECOND_PLAYER_MARK
