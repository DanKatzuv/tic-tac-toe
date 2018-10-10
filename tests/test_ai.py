from itertools import product

from pytest import mark

from board.board import Board
from game import Game
from players import AI


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_first_turn(player_mark):
    ai = AI(player_mark)
    board = Board()
    assert ai._first_turn(board.representation()) in product((0, 2), (0, 2))


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_second_turn_corner_opening(player_mark):
    other_mark = Game.FIRST_PLAYER_MARK
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._rows = [[' ', ' ', other_mark],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._rows = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', other_mark]]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._rows = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [other_mark, ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_second_turn_center_opening(player_mark):
    other_mark = Game.FIRST_PLAYER_MARK
    ai = AI(player_mark)
    board = Board()
    board._rows = [[' ', ' ', ' '],
                   [' ', other_mark, ' '],
                   [' ', ' ', ' ']]
    for _ in range(100):
        assert ai._second_turn(board.representation()) in product((0, 2), (0, 2))


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_win(player_mark):
    ai = AI(player_mark)
    board = Board()
    board._rows = [[player_mark, ' ', player_mark],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (0, 1)

    board._rows = [[' ', player_mark, ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (2, 1)

    board._rows = [[' ', ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', player_mark]]
    assert ai.turn(board.representation()) == (0, 0)

    board._rows = [[' ', ' ', player_mark],
                   [' ', ' ', ' '],
                   [player_mark, ' ', ' ']]
    assert ai.turn(board.representation()) == (1, 1)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_block(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', other_mark],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (0, 1)

    board._rows = [[' ', other_mark, ' '],
                   [' ', other_mark, ' '],
                   [' ', ' ', ' ']]
    assert ai.turn(board.representation()) == (2, 1)

    board._rows = [[' ', ' ', ' '],
                   [' ', other_mark, ' '],
                   [' ', ' ', other_mark]]
    assert ai.turn(board.representation()) == (0, 0)

    board._rows = [[' ', ' ', other_mark],
                   [' ', ' ', ' '],
                   [other_mark, ' ', ' ']]
    assert ai.turn(board.representation()) == (1, 1)

    board._rows = [[player_mark, ' ', ' '],
                   [other_mark, other_mark, ' '],
                   [player_mark, ' ', other_mark]]
    assert ai.turn(board.representation()) == (1, 2)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_create_fork(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[player_mark, ' ', ' '],
                   [' ', other_mark, ' '],
                   [' ', ' ', player_mark]]
    assert ai.turn(board.representation()) in ((2, 0), (0, 2))

    board._rows = [[player_mark, ' ', ' '],
                   [player_mark, ' ', ' '],
                   [' ', ' ', ' ']]
    assert ai._fork(board.representation()) == (1, 1)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_block_fork(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', other_mark]]
    assert ai.turn(board.representation()) in ((0, 2), (2, 0))

    board._rows = [[player_mark, ' ', ' '],
                   [' ', other_mark, ' '],
                   [' ', ' ', other_mark]]
    assert ai.turn(board.representation()) in ((0, 2), (2, 0))


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_center(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', other_mark]]
    assert ai._center(board.representation()) is None

    board._rows = [[player_mark, ' ', ' '],
                   [' ', ' ', ' '],
                   [other_mark, ' ', other_mark]]
    assert ai._center(board.representation()) == (1, 1)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_opposite_corner(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', ' ']]
    assert ai._opposite_corner(board.representation()) == (2, 2)

    board._rows = [[player_mark, ' ', ' '],
                   [' ', ' ', ' '],
                   [other_mark, ' ', other_mark]]
    assert ai._opposite_corner(board.representation()) == (0, 2)

    board._rows = [[player_mark, ' ', player_mark],
                   [' ', ' ', ' '],
                   [other_mark, ' ', other_mark]]
    assert ai._opposite_corner(board.representation()) is None


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_empty_corner(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', ' ', ' ']]
    assert ai._empty_corner(board.representation()) in ((0, 2), (2, 2), (2, 0))

    board._rows = [[player_mark, ' ', ' '],
                   [' ', ' ', ' '],
                   [other_mark, ' ', other_mark]]
    assert ai._empty_corner(board.representation()) == (0, 2)

    board._rows = [[player_mark, ' ', player_mark],
                   [' ', ' ', ' '],
                   [other_mark, ' ', other_mark]]
    assert ai._empty_corner(board.representation()) is None


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_empty_edge(player_mark):
    other_mark = other_player(player_mark)
    ai = AI(player_mark)
    board = Board()
    board._rows = [[other_mark, ' ', ' '],
                   [' ', player_mark, ' '],
                   [' ', player_mark, ' ']]
    assert ai._empty_edge(board.representation()) in ((0, 1), (1, 2), (1, 0))

    board._rows = [[player_mark, other_mark, ' '],
                   [' ', ' ', ' '],
                   [other_mark, player_mark, other_mark]]
    assert ai._empty_edge(board.representation()) in ((1, 2), (1, 0))

    board._rows = [[player_mark, player_mark, player_mark],
                   [other_mark, ' ', player_mark],
                   [other_mark, other_mark, other_mark]]
    assert ai._empty_edge(board.representation()) is None


def other_player(player_mark):
    """
    Return the other player's mark, based on the given mark.

    :param player_mark: mark of this player
    :type player_mark:
    :return: mark of the other player
    :rtype: str
    """
    return Game.FIRST_PLAYER_MARK if player_mark == Game.SECOND_PLAYER_MARK else Game.SECOND_PLAYER_MARK
