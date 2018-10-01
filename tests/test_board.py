from pytest import mark

from board.board import Board


@mark.parametrize('mark', ('X', 'O'))
def test_row(mark):
    board = Board()
    board._board = [[' ', ' ', ' '],
                    [mark, mark, mark],
                    [' ', ' ', ' ']]

    for column in range(3):
        assert board._has_win_occurred(1, column)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 1)
    assert not board._has_win_occurred(2, 2)


@mark.parametrize('mark', ('X', 'O'))
def test_column(mark):
    board = Board()
    board._board = [[' ', mark, ' '],
                    [' ', mark, ' '],
                    [' ', mark, ' ']]

    for row in range(3):
        assert board._has_win_occurred(row, 1)
    assert not board._has_win_occurred(0, 2)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 2)


@mark.parametrize('mark', ('X', 'O'))
def test_main_diagonal(mark):
    board = Board()
    board._board = [[mark, ' ', ' '],
                    [' ', mark, ' '],
                    [' ', ' ', mark]]

    for row in range(3):
        assert board._has_win_occurred(row, row)
    assert not board._has_win_occurred(0, 2)
    assert not board._has_win_occurred(2, 0)
    assert not board._has_win_occurred(2, 1)


@mark.parametrize('mark', ('X', 'O'))
def test_secondary_diagonal(mark):
    board = Board()
    board._board = [[' ', ' ', mark],
                    [' ', mark, ' '],
                    [mark, ' ', ' ']]

    for row in range(3):
        assert board._has_win_occurred(row, 2 - row)
    assert not board._has_win_occurred(0, 0)
    assert not board._has_win_occurred(2, 2)
    assert not board._has_win_occurred(1, 0)


def test_is_board_full():
    board = Board()
    board._board = [['X', 'O', 'X'],
                    ['O', 'X', 'O'],
                    ['X', 'O', 'X']]
    assert board.is_full()
