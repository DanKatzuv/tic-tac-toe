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
    board._board = [[other_mark, ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._board = [[' ', ' ', other_mark],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._board = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', other_mark]]
    assert ai._second_turn(board.representation()) == (1, 1)

    board._board = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [other_mark, ' ', ' ']]
    assert ai._second_turn(board.representation()) == (1, 1)


@mark.parametrize('player_mark', (Game.FIRST_PLAYER_MARK, Game.SECOND_PLAYER_MARK))
def test_second_turn_center_opening(player_mark):
    other_mark = Game.FIRST_PLAYER_MARK
    ai = AI(player_mark)
    board = Board()
    board._board = [[' ', ' ', ' '],
                    [' ', other_mark, ' '],
                    [' ', ' ', ' ']]
    for _ in range(100):
        assert ai._second_turn(board.representation()) in product((0, 2), (0, 2))
